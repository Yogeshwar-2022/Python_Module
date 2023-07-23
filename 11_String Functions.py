Story = '''going back to the corner where I first saw you
gonna camp in my sleeping bag I'm not gonna move
Got some words on cardboard, got your picture in my hand
Saying, "if you see this girl can you tell her where I am?" '''
print(Story)

# String functions

print(len(Story))

print(Story.endswith('''not gonna move'''))
print(Story.endswith('''where I am?" '''))

print(Story.count("z"))
print(Story.count("in"))

print(Story.capitalize())

print(Story.find('in'))
print(Story.find('corner'))
print(Story.find('inside'))

print(Story.replace("in", "BISH"))