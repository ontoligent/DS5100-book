# Prevents you from having to write import funny.funniest 
# ----------------------
# import funny
# funny.joke()
# funny.funniest.joke()
# from funny import joke
# joke()
# ----------------------
# from funny.funniest import joke
from . funniest import joke 

# ----------------------
# import funny
# funny.funniest.joke()
# ----------------------
import funny.funniest

print("Import 20")
