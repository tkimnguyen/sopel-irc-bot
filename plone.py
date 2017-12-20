import sopel.module

REGULARS = ['[Arfrever]', 'alxd', 'Arminder', 'ArminderSingh', 'bloodbare', 'claytron', 
	'cuongnda', 'cwarner', 'danima1', 'datakurre', 'davidsapiro', 'djinni', 'domenkozar', 
	'encolpe', 'esteele', 'frapell', 'gl278afd', 'glimmung', 'goibhniu', 'Gomez', 
	'Hazelesque', 'hng23', 'isp_[m]', 'jakob_', 'jfroche', 'jham', 'jpcw', 'kaeru', 
	'kiorky', 'kuetrzi', 'lem-fr', 'lentinj', 'malthe', 'martior', 'matthewwilkes', 
	'mcdonc', 'merpdotcom', 'moldy', 'moo-_-', 'nii', 'nopf', 'pbauer', 'pcdummy', 
	'pysailor', 'rainrider', 'ree', 'regebro', 'rnix', 'robink', 'robmyers', 'rockfruit', 
	'roq_', 'Rotonen', 'sallyk', 'santonelli', 'siel', 'SopelBot', 'SteveM', 
	'stevepiercy', 'svx', 'tibi', 'tkimnguyen', 'tsimkins', 'zombified',] 

@sopel.module.commands('echo', 'repeat')
def echo(bot, trigger):
    """Repeat what was said to me"""
    bot.reply(trigger.group(2))

# not sure why this doesn't work
@sopel.module.rule('hello')
def hi(bot, trigger):
    """Say hi back"""
    bot.say('Hi, ' + trigger.nick)

@sopel.module.commands('helloworld')
def helloworld(bot, trigger):
    """Greet the world"""
    bot.say('Hello, world!')

@sopel.module.rule('.*[^.]?help.*')
def hi(bot, trigger):
    """Response when someone (who is not a regular \#plone member) asks for help"""
    if trigger.nick not in REGULARS:
	    bot.reply('Welcome! Please read https://plone.org/support for tips on how to ask for help. Our forum https://community.plone.org is the best place to ask detailed questions, where more people will see them and be able to answer. For emergency support, contact commercial Plone providers at https://plone.com/providers')
    #else:
            #bot.reply('You know the drill...')

