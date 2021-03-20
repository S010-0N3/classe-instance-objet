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
