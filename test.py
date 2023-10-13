from libgen_api_li import LibgenSearch
import json

s = LibgenSearch()

results = s.search_author("Peter Hoffman")
print(results)
save_file = open("savedata.json", "w")
json.dump(results, save_file, indent=6)
save_file.close()
