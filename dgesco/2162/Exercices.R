

# Importer des données ----------------------------------------------------
# Exercice 1
Communes =
  read.table(
    file = "Communes.txt",
    header = TRUE,
    sep = "|",
    quote = "\"",
    strip.white = TRUE,
    blank.lines.skip = TRUE
  )

Agents =
  read.table(
    file = "Agents.csv",
    header = TRUE,
    sep = ";",
    quote = "",
    blank.lines.skip = TRUE,
    strip.white = TRUE
  )

# Exercice 2
require(haven)
BCE =
  read_sas(data_file = "bce_uai.sas7bdat")

# Exercice 3
require(jsonlite)
Service =
  fromJSON(txt = "Service.json")

# Exercice 4
require(readxl)
excel_sheets("Geoloc.xlsx")
Departements =
  read_excel(path = "Geoloc.xlsx",
             sheet = "Departements")
ACADEMIES =
  read_excel(path = "Geoloc.xlsx",
             sheet = "ACADEMIES")
Regions =
  read_excel(path = "Geoloc.xlsx",
             sheet = "Regions")
