products = {
  "Cortex": ["What Cortex product are you interested in?", "Are you looking to purchase?", "Are you troubleshooting?"],
  "Strata": ["Do you own NGFWs today?", "Are you deployed on prem or in the cloud?"],
  "Prisma": ["Do you have multiple cloud providers?", "What are your deployments?"]
}

prompt = """
What product do you need help with today?\n
1. Cortex
2. Strata
3. Prisma

Enter number to proceed
"""

selection = int(input(prompt))
if selection not in [1,2,3]:
  selection = 1

product = list(products.keys())[selection-1]

print(f"It looks like you are interested in {product}")

answers = []

for question in products[product]:
  answers.append(input(question))

print("Excellent thanks for your answers we are following up with a specialist!")

body = '<br/>'.join([f'<p>{products[product][index]} ' + answer + '</p>' for index, answer in enumerate(answers)])

html = f"""
<!DOCTYPE html>
<html>
  <body>
    <h1>{product} Survey</h1>
    {body}
  </body>
</html>
"""

with open("index.html", "w") as f:
  f.write(html)

print(html)
