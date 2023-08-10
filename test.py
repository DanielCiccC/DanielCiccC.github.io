# Don't cheat >:(
def really_spooky(n):
  if n == 20:
    return n
  return really_spooky(n + 1) + really_spooky(n - 1)

really_spooky(50) #this is the call 