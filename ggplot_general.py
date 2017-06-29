__author__ = 'albertogonzalez'

'''
http://ggplot.yhathq.com/docs/index.html
'''
from ggplot import *

# bivariate data with stat smooth
ggplot(aes(x='date', y='beef'), data=meat) + geom_line() + stat_smooth(colour='blue', span=0.2)

# Bivariate wuth scale diverging
ggplot(diamonds, aes(x='carat', y='price', color='cut')) + geom_point() + scale_color_brewer(type='diverging', palette=4) + xlab("Carats") + ylab("Price") + ggtitle("Diamonds")

# Facet
ggplot(diamonds, aes(x='price', fill='cut')) + geom_density(alpha=0.25) + facet_wrap("clarity")

# Geom abline
ggplot(mtcars,aes(x='wt',y='mpg')) + geom_point() + geom_abline(intercept=20)

# Geom area
ggplot(aes(x='date', ymin='beef - 1000', ymax='beef + 1000'), data=meat) + geom_area()

# Geom bar
ggplot(aes(x='factor(cyl)'), data=mtcars) + geom_bar()

# Geom density
ggplot(aes(x='pageviews'), data=pageviews) + geom_density()

# Facet: facet_grid(x_facet, y_facet, scales = "fixed")
ggplot(aes("price","depth"),data=diamonds) + geom_point() + facet_grid(x="clarity",y="color")

# Themes: seaborn, bw, gray, matplotlib, xkcd
ggplot(aes("price","depth"),data=diamonds) + geom_point() + theme_seaborn()



