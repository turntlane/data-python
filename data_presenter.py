
import plotly.graph_objects as go



data = open('CupcakeInvoices.csv')

chocolate = 0
vanilla = 0
strawberry = 0


total = 0
for length in data:
  # print(length)
  length = length.rstrip('\n').split(',')
  sum = float(length[3]) * float(length[4])
  total += sum
  print(length[2]) 
  print(round(sum, 2))

  if length[2] == 'Chocolate':
    chocolate += sum
  elif length[2] == 'Vanilla':
    vanilla += sum
  elif length[2] == 'Strawberry':
    strawberry += sum


print('The total is: ' + str(round(total, 2)))



fig = go.Figure(data=go.Bar(y=[chocolate, vanilla, strawberry],x=["Chocolate", "Vanilla", "Strawberry"]))

fig.show()









# import matplotlib.pyplot as plt
# import pandas as pd


# df = pd.read_csv('CupcakeInvoices.csv')

# x = df['Chocolate', 'Vanilla', 'Strawberry']
# y = df[total]


# plt.xlabel('Chocolate', 'Vanilla', 'Strawberry', fontsize=18)
# plt.ylabel(total, fontsize=18)
# plt.bar(x, y)

# plt.show()



    





