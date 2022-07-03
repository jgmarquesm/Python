# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15

warn_the_sheep = lambda queue: "Pls go away and stop eating my sheep" if "wolf" == queue[-1] else f"Oi! Sheep number {len(queue) - queue.index('wolf') - 1}! You are about to be eaten by a wolf!"
