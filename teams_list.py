teams = ('Flamengo', 'Internacioonal', 'Atlético-MG', 'Sao-paulo', 'Fluminense',
         'Gremio', 'Palmeiras', 'Santos', 'Athletico Paranaense', 'Bragantino',
          'Ceara', 'Corinthians', 'Atletico-GO', 'Bahia', 'Sport', 'Fortaleza',
          'Vasco', 'Goias', 'Coritiba', 'Botafogo')

print(f'Brasileirao list: {teams}')
print('=' * 100)
print(f'The first five are: {teams[0 : 5]}')
print('=' * 100)
print(f'The last four are: {teams[-1:-5:-1]}')
print('=' * 100)
print(f'Teams in alphabetic order: {sorted(teams)}')
print('=' * 100)
print(f'Palmeiras is in the position: {teams.index("Palmeiras") + 1}º')
print('=' * 100)
