from libgen_api_li import LibgenSearch

s = LibgenSearch()

results = s.search_author("Peter Hoffman")
print(results)