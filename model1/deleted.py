
elif len(r) == 0 or r is None:
			context = {'com': 'No Player Found'}

		elif len(r) == 1:
			context = {'com': r}

		elif r != '' and request.POST.get("number_field") == '':
			#name typed in, empty number = more than 1 person for name
			context = {'com': 'Name not specific enough'}

else: # r is hella names 
			if request.POST.get("number_field") == '' and request.POST.get("team_field") == '':			
				context = {'com': 'Enter jersey number or team'}				
			else:
				num = request.POST.get("number_field")
				if request.POST.get("team_field") == '':
					context = {'com': 'Please enter team code'}		
				else:
					team = request.POST.get("team_field")
					team_id = statsapi.lookup_team(team)
					for player in r:
						if player['primaryNumber'] == num and player['currentTeam'] == team_id:
							context = {'com': player}
							return render(request, "model1/results.html", context)	
					context = {'com': 'No Player with desired number on {}'.format(team)}		
		return render(request, "model1/results.html", context)



		elif len(r) == 0 or r is None:
			context = {'com': 'No Player Found'}

		elif len(r) == 1:
			context = {'com': r}

		elif r != '' and request.POST.get("number_field") == '':
			#name typed in, empty number = more than 1 person for name
			context = {'com': 'Name not specific enough'}

		else: # r is hella names 
			if request.POST.get("number_field") == '' and request.POST.get("team_field") == '':			
				context = {'com': 'Enter jersey number or team'}				
			else:
				num = request.POST.get("number_field")
				if request.POST.get("team_field") == '':
					context = {'com': 'Please enter team code'}		
				else:
					team = request.POST.get("team_field")
					team_id = statsapi.lookup_team(team)
					for player in r:
						if player['primaryNumber'] == num and player['currentTeam'] == team_id:
							context = {'com': player}
							return render(request, "model1/results.html", context)	
					context = {'com': 'No Player with desired number on {}'.format(team)}	



# results

<!DOCTYPE html>
<html lang="en"> <!-- hover over row numbers to collapse/expand chunks -->
	<head>
		<meta charset="UTF-8">
		<title>Tab Test</title>
		{% load static %}
		<link rel="stylesheet" type="text/css" href="{% static 'model1/style2.css' %}">
	</head>
	<body> <!--  everything appears in the body pretty much -->
		{% for player in com %}
		<header>
			<img src="https://securea.mlb.com/images/players/action_shots/{{ player.id }}.jpg" class="card-img-top" alt="Responsive image" alt="Toronto Skyline"> 
		</header>

		<main> <!-- this is a structuring element that helps separate things -->

		<img src="https://securea.mlb.com/mlb/images/players/head_shot/{{ player.id }}.jpg" class="img-fluid" alt="Responsive image">
		<br><br>
		Name: {{ player.fullName }}


		{% endfor %}

		<button type="button" class="btn btn-primary btn-lg btn-block">Block level button</button>

		<h1> Toronto Blue Jays </h1> <!--  h1 is a large heading -->
		
		<p> MLB Profile <a href="https://www.mlb.com/bluejays">'anchor' for jays' site </a>  </p>

		<h2>Players and Coaches</h2> <!-- h2 is another type of heading -->

		<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
		tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
		quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
		consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
		cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
		proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

		</main>

		<footer>
			Copyright, GA Bitmaker, 2019
		</footer>
	</body>
</html>