def draw(percent):
    thick_bar = '▓'
    thin_bar = '░'
    bar = percent * thick_bar + (100 - percent) * thin_bar
    print(bar + ' ' + str(percent) + '%')
