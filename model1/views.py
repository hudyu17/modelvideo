from django.shortcuts import render, redirect
from .home import PlayerInput
import requests
import json
import statsapi


def results(request):
	
	# url = "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&name_part={}"
	# url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

	if request.method == 'POST':

		r = statsapi.lookup_player(request.POST.get("name_field")) # search by name first
		# returns a list - if so, can work in r[0] for succ contexts

		# case 1: all 3 provided
		if (request.POST.get("name_field") != '' and request.POST.get("number_field") != ''\
		and request.POST.get("team_field") != ''):
			num = request.POST.get("number_field")
			team = request.POST.get("team_field")
			team_list_dict = statsapi.lookup_team(team)
			
			if len(team_list_dict) == 0:
				context = {'com': 'Inconsistent information - team does not exist'}

			else:
				players = []
				for player in r:
					if len(team_list_dict) == 1:
						team_id = team_list_dict[0]['id']
						if player['primaryNumber'] == num and player['currentTeam']['id'] == team_id:
							players.append(player)
					else:  # len(team_list_dict) > 1
						for ind_team in team_list_dict:
							team_id = ind_team['id']
							if player['primaryNumber'] == num and player['currentTeam']['id'] == team_id:
								players.append(player)

				if len(players) == 1:
					context = {'com': players}  
				elif len(players) > 1: 
					context = {'com': 'Too broad - make information more specific'}
				else:
					context = {'com': 'No player found - possibly inconsisent information'}

		# case 2: no info provided

		elif (request.POST.get("name_field") == '' and request.POST.get("number_field") == ''\
		and request.POST.get("team_field") == ''):
			context = {'com': 'No information given'}

		# case 3: name only 
		elif (request.POST.get("name_field") != '' and request.POST.get("number_field") == ''\
		and request.POST.get("team_field") == ''):
			print(r)
			if len(r) == 1:   # 1 player only
				context = {'com': r}
			elif len(r) > 1:  # more than 1 player 
				context = {'com': 'Too broad - add player information'}
			else:  # no players
				context = {'com': 'No player found'}

		# case 4: name, number
		elif (request.POST.get("name_field") != '' and request.POST.get("number_field") != ''\
		and request.POST.get("team_field") == ''):
			num = request.POST.get("number_field")
			players = []

			for player in r:
				try:
					if player['primaryNumber'] == num:  # both strings so ok
						players.append(player)
				except:
					pass
			
			if len(players) == 1:
				context = {'com': players}  # or players[0], but i think im right
			elif len(players) > 1: 
				context = {'com': 'Too broad - add player information'}
			else:
				context = {'com': 'No player found'}

		# case 5: name, team
		elif (request.POST.get("name_field") != '' and request.POST.get("number_field") == ''\
		and request.POST.get("team_field") != ''):
			team = request.POST.get("team_field")
			team_list_dict = statsapi.lookup_team(team)
			
			if len(team_list_dict) == 0:
				context = {'com': 'Inconsistent information - team does not exist'}

			else:
				players = []
				for player in r:
					if len(team_list_dict) == 1:
						team_id = team_list_dict[0]['id']
						if player['currentTeam']['id'] == team_id:
							players.append(player)
					else:  # len(team_list_dict) > 1
						for ind_team in team_list_dict:
							team_id = ind_team['id']
							if player['currentTeam']['id'] == team_id:
								players.append(player)

				if len(players) == 1:
					context = {'com': players}  
				elif len(players) > 1: 
					context = {'com': 'Too broad - multiple players share parts of this name'}
				else:
					context = {'com': 'No player found'}

		# case 6: number only 
		elif (request.POST.get("name_field") == '' and request.POST.get("number_field") != ''\
		and request.POST.get("team_field") == ''):
			num = request.POST.get("number_field")
			number_list_dict = statsapi.lookup_player(num)
			players = []

			for player in number_list_dict:
				try:
					if player['primaryNumber'] == num:  
						players.append(player)
				except:
					pass

			if len(players) == 1:
				context = {'com': players} 
			elif len(players) > 1: 
				context = {'com': 'Too broad - add player information'}
			else:
				context = {'com': 'No player found - no player holds this jersey number'}

		# case 7: number, team
		elif (request.POST.get("name_field") == '' and request.POST.get("number_field") != ''\
		and request.POST.get("team_field") != ''):
			
			num = request.POST.get("number_field")
			number_list_dict = statsapi.lookup_player(num)

			team = request.POST.get("team_field")
			team_list_dict = statsapi.lookup_team(team)

			if len(team_list_dict) == 0:
				context = {'com': 'Inconsistent information - team does not exist'}

			elif len(number_list_dict) == 0:
				context = {'com': 'No player found - no player holds this jersey number'}

			else:
				players = []

				for player in number_list_dict:
					try:
						if player['primaryNumber'] == num:  
							players.append(player)
					except:
						pass

				players2 = []
				for player in players:
					if len(team_list_dict) == 1:
						team_id = team_list_dict[0]['id']
						if player['currentTeam']['id'] == team_id:
							players2.append(player)
					else:  # len(team_list_dict) > 1
						for ind_team in team_list_dict:
							team_id = ind_team['id']
							if player['currentTeam']['id'] == team_id:
								players2.append(player)
				
				if len(players2) == 1:
					context = {'com': players2}  
				elif len(players2) > 1:  #lowkey impossible for multiple numbers on same team
					context = {'com': 'Too broad - multiple players share this jersey number'}
				else:
					context = {'com': 'No player found - no player on this team holds this jersey number'}

		# case 8: team only
		elif (request.POST.get("name_field") == '' and request.POST.get("number_field") == ''\
		and request.POST.get("team_field") != ''):
			team = request.POST.get("team_field")
			team_list_dict = statsapi.lookup_team(team)

			if len(team_list_dict) == 0:
				context = {'com': 'Inconsistent information - team does not exist'}
			else:
				context = {'com': 'Too broad - multiple players found on team'}


		return render(request, "model1/results.html", context)

	else:
		# context = {'com': PlayerInput()}
		return render(request, "model1/home.html", {})


def home(request):
	return render(request, "model1/home.html", {})

