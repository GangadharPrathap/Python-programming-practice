def find_winner(india_points, australia_points, india_matches, australia_matches):
  if(india_points>australia_points):
    print("India")
  if(india_points<australia_points):
    print("Australia")
  if(india_points==australia_points):
    if(india_matches>australia_matches):
      print("India")
    if(india_matches<australia_matches):
      print("Australia")
    if(india_matches==australia_matches):
      print("Play another game")
india_points=int(input())
australia_points=int(input())
india_matches=int(input())
australia_matches=int(input())
find_winner(india_points, australia_points, india_matches, australia_matches)