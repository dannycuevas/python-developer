mark = int(input('Provide your test mark: '))

if mark >= 7:
  print('Grade A')
  print('End of first IF statement')
else:
  if mark <= 5:
    print('This is bad, you failed!')
    print('I mean, like real bad lol')
  else:
    print('Grade B')
    print('You passed, but you can do better!')

print('End of program for marks. Good luck.')
