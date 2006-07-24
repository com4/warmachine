import say, op, deop, quit, part, voice, devoice
import join, kick, pythondoc, settopic, coin

actions = {}
actions['say']       = say.say()
actions['op']        = op.op()
actions['deop']      = deop.deop()
actions['quit']      = quit.quit()
actions['part']      = part.part()
actions['voice']     = voice.voice()
actions['devoice']   = devoice.devoice()
actions['kick']      = kick.kick()
actions['join']      = join.join()
actions['pythondoc'] = pythondoc.pythondoc()
actions['settopic']  = settopic.settopic()
actions['coin']      = coin.coin()
