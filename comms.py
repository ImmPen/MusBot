async def clear(cntx):
    await cntx.channel.purge()

comms = {"clear": clear}

async def commHandler(cntx):
    try:
        return await comms[cntx.content[1:]](cntx)
    except:
        return
    