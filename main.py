import csv

f = open("nfl_data.csv")
nfl = csv.reader(f)

#je creer une classe team 

class Team():
  def __init__(self, name):
    self.name = name

  def print_name(self):
    print(self.name)

  def count_total_wins(self):
    count = 0
    for row in nfl:
      if row[2] == self.name:
        count += 1
    return(count)


# je transforme la variable brancos en objet de la classe Team() pour pouvoir utiliser ces methode de classe.
broncos = Team("Denver Broncos")

# j'utilise une methode de la classe Team()

broncos_wins = broncos.count_total_wins()

#j'affiche le resultat

print(broncos_wins)

#Améliorer la méthode d'instance __init__
import csv


class Team():
  def __init__(self, name):
    self.name = name
    f = open("nfl_data.csv")
    csvreader = csv.reader(f)
    self.nfl= list(csvreader)

  def print_name(self):
    print(self.name)

  def count_total_wins(self):
    count = 0
    for row in self.nfl:
      if row[2] == self.name:
        count += 1
    return(count)


sf = Team("San Francisco 49ers")
sf_wins =sf.count_total_wins()
print(sf_wins)




# ajout methode calculant les victoire selon l'anne
class Team():
  def __init__(self, name):
    self.name = name
    f = open("nfl_data.csv")
    csvreader = csv.reader(f)
    self.nfl= list(csvreader)

  def print_name(self):
    print(self.name)

  def count_total_wins(self):
    count = 0
    for row in self.nfl:
      if row[2] == self.name:
        count += 1
    return(count)

  def count_wins_in_year(self,year):
    self.year = year
    count = 0
    for row in self.nfl:
      if row[2] == self.name and row[0] == year:
        count += 1
    return(count)


sf = Team("San Francisco 49ers")
sf_wins =sf.count_wins_in_year("2012")
print(sf_wins)