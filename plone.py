import sopel.module

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
    """Response when someone asks for help"""
    bot.reply('Welcome! Please read https://plone.org/support for tips on how to ask for help. Our forum https://community.plone.org is the best place to ask detailed questions, where more people will see them and be able to answer. For emergency support, contact commercial Plone providers at https://plone.com/providers')

