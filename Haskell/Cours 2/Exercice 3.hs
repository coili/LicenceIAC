savants = (("Curry","Haskell"),("Newton","Isaac"),
          ("Currie","Marie"),("Turing","Alan"),("Tesla","Nikola"),
          ("Einstein","Albert"))

((_, _), (_, prenom2), (_, prenom3), (_, prenom4), (_, prenom5), (_, prenom6)) = savants

prenomsSavants = (prenom2, prenom3, prenom4, prenom5, prenom6)

main = do
    print prenomsSavants