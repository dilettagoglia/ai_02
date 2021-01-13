from data_structure import gameStatus
from data_structure.gameStatus import *


def lowLevelStrategy(maxWeight, endx, endy):
    # Here self refers to karen
    """
    Basic strategy function
    :return: the next action(s) that the players have to do.
    """
    # Array di coppie <action,direction>     (i.e. <move, N> , <shoot,E> ...)
    nextActions = []
    try:
        direction, coordinates = gameStatus.game.me.movement.move(gameStatus.game.weightedMap, gameStatus.game.me, endx, endy)
    except():
        print("Exception generated by movement.move")
        return nextActions

    # se sto in linea con altri, sparo
    for key in gameStatus.game.enemies:
        enemy = gameStatus.game.enemies.get(key)

        if enemy.state == "ACTIVE" and gameStatus.game.weightedMap[gameStatus.game.me.y][gameStatus.game.me.x] == int(maxWeight / 2):
            if gameStatus.game.me.x == enemy.x:
                if gameStatus.game.me.y > enemy.y:
                    nextActions.append(("shoot", "N"))
                else:
                    nextActions.append(("shoot", "S"))
            elif gameStatus.game.me.y == enemy.y:

                if gameStatus.game.me.x > enemy.x:
                    nextActions.append(("shoot", "W"))
                else:
                    nextActions.append(("shoot", "E"))

    # controllo se andrò in linea di tiro
    if direction == "E" and gameStatus.game.weightedMap[gameStatus.game.me.y][gameStatus.game.me.x + 1] == int(maxWeight / 2):

        # my x becomes  x+1
        if gameStatus.game.serverMap[gameStatus.game.me.y][gameStatus.game.me.x + 1] == "~":
            nextActions.append(("move", direction))

        else:
            for key in gameStatus.game.enemies:
                enemy = gameStatus.game.enemies.get(key)

                if enemy.x == gameStatus.game.me.x + 1:

                    if enemy.y >= gameStatus.game.me.y:
                        # muoviti ad est e spara a sud
                        nextActions.append(("move", direction))
                        nextActions.append(("shoot", "S"))

                    if enemy.y < gameStatus.game.me.y:
                        # muoviti ad est e spara a nord
                        nextActions.append(("move", direction))
                        nextActions.append(("shoot", "N"))


    elif direction == "W" and gameStatus.game.weightedMap[gameStatus.game.me.y][gameStatus.game.me.x - 1] == int(maxWeight / 2):

        # my x becomes  x-1
        if gameStatus.game.serverMap[gameStatus.game.me.y][gameStatus.game.me.x - 1] == "~":
            nextActions.append(("move", direction))
        else:
            for key in gameStatus.game.enemies:
                enemy = gameStatus.game.enemies.get(key)

                if enemy.x == gameStatus.game.me.x - 1:

                    if enemy.y >= gameStatus.game.me.y:
                        # muoviti ad ovest e spara a sud
                        nextActions.append(("move", direction))
                        nextActions.append(("shoot", "S"))

                    if enemy.y < gameStatus.game.me.y:
                        # muoviti ad ovest e spara a nord
                        nextActions.append(("move", direction))
                        nextActions.append(("shoot", "N"))


    elif direction == "S" and gameStatus.game.weightedMap[gameStatus.game.me.y + 1][gameStatus.game.me.x] == int(maxWeight / 2):

        # my y becomes  y+1
        if gameStatus.game.serverMap[gameStatus.game.me.y + 1][gameStatus.game.me.x] == "~":
            nextActions.append(("move", direction))
        else:
            for key in gameStatus.game.enemies.keys():
                enemy = gameStatus.game.enemies.get(key)

                if enemy.y == gameStatus.game.me.y + 1:

                    if enemy.x >= gameStatus.game.me.x:
                        nextActions.append(("move", direction))
                        nextActions.append(("shoot", "E"))

                    if enemy.x < gameStatus.game.me.x:
                        # muoviti a sud e spara ad ovest
                        nextActions.append(("move", direction))
                        nextActions.append(("shoot", "W"))



    elif direction == "N" and gameStatus.game.weightedMap[gameStatus.game.me.y - 1][gameStatus.game.me.x] == int(maxWeight / 2):

        # my y becomes  y-1
        if gameStatus.game.serverMap[gameStatus.game.me.y - 1][gameStatus.game.me.x] == "~":
            nextActions.append(("move", direction))

        else:
            for key in gameStatus.game.enemies:
                enemy = gameStatus.game.enemies.get(key)

                if enemy.y == gameStatus.game.me.y - 1:

                    if enemy.x > gameStatus.game.me.x:
                        # muoviti ad nord e spara ad est
                        nextActions.append(("move", direction))
                        nextActions.append(("shoot", "E"))

                    if enemy.x < gameStatus.game.me.x:
                        # muoviti a nord e spara ad ovest
                        nextActions.append(("move", direction))
                        nextActions.append(("shoot", "W"))


    # Non sono andato in linea di tiro
    else:
        nextActions.append(("move", direction))

    return nextActions


def lowLevelStrategyImpostor(self, endx, endy):
    # Here self refers to karen
    """
    Basic strategy function
    :return: the next action(s) that the players have to do.
    """
    # Array di coppie <action,direction>     (i.e. <move, N> , <shoot,E> ...)
    nextActions = []
    try:
        direction, coordinates = gameStatus.game.me.movement.move(gameStatus.game.weightedMap, gameStatus.game.me, endx, endy)
    except():
        print("Exception generated by movement.move")
        return nextActions



    # se sto in linea con altri, sparo
    if gameStatus.game.activeAllies < len(gameStatus.game.allies)/3:
        for key in gameStatus.game.allies:
            ally = gameStatus.game.allies.get(key)

            if ally.state == "ACTIVE" and gameStatus.game.weightedImpostorMap[gameStatus.game.me.y][gameStatus.game.me.x] == int(self.maxWeight / 2):
                if gameStatus.game.me.x == ally.x:
                    if gameStatus.game.me.y > ally.y:
                        nextActions.append(("shoot", "N"))
                    else:
                        nextActions.append(("shoot", "S"))
                elif gameStatus.game.me.y == ally.y:

                    if gameStatus.game.me.x > ally.x:
                        nextActions.append(("shoot", "W"))
                    else:
                        nextActions.append(("shoot", "E"))

        # controllo se andrò in linea di tiro
        if direction == "E" and gameStatus.game.weightedImposotrMap[gameStatus.game.me.y][gameStatus.game.me.x + 1] == int(self.maxWeight / 2):

            # my x becomes  x+1
            if gameStatus.game.serverMap[gameStatus.game.me.y][gameStatus.game.me.x + 1] == "~":
                nextActions.append(("move", direction))

            else:
                for key in gameStatus.game.allies:
                    ally = gameStatus.game.allies.get(key)

                    if ally.x == gameStatus.game.me.x + 1:

                        if ally.y >= gameStatus.game.me.y:
                            # muoviti ad est e spara a sud
                            nextActions.append(("move", direction))
                            nextActions.append(("shoot", "S"))

                        if ally.y < gameStatus.game.me.y:
                            # muoviti ad est e spara a nord
                            nextActions.append(("move", direction))
                            nextActions.append(("shoot", "N"))


        elif direction == "W" and gameStatus.game.weightedImpostorMap[gameStatus.game.me.y][gameStatus.game.me.x - 1] == int(self.maxWeight / 2):

            # my x becomes  x-1
            if gameStatus.game.serverMap[gameStatus.game.me.y][gameStatus.game.me.x - 1] == "~":
                nextActions.append(("move", direction))
            else:
                for key in gameStatus.game.allies:
                    ally = gameStatus.game.allies.get(key)

                    if ally.x == gameStatus.game.me.x - 1:

                        if ally.y >= gameStatus.game.me.y:
                            # muoviti ad ovest e spara a sud
                            nextActions.append(("move", direction))
                            nextActions.append(("shoot", "S"))

                        if ally.y < gameStatus.game.me.y:
                            # muoviti ad ovest e spara a nord
                            nextActions.append(("move", direction))
                            nextActions.append(("shoot", "N"))


        elif direction == "S" and gameStatus.game.weightedImpostorMap[gameStatus.game.me.y + 1][gameStatus.game.me.x] == int(self.maxWeight / 2):

            # my y becomes  y+1
            if gameStatus.game.serverMap[gameStatus.game.me.y + 1][gameStatus.game.me.x] == "~":
                nextActions.append(("move", direction))
            else:
                for key in gameStatus.game.allies.keys():
                    ally = gameStatus.game.allies.get(key)

                    if ally.y == gameStatus.game.me.y + 1:

                        if ally.x >= gameStatus.game.me.x:
                            nextActions.append(("move", direction))
                            nextActions.append(("shoot", "E"))

                        if ally.x < gameStatus.game.me.x:
                            # muoviti a sud e spara ad ovest
                            nextActions.append(("move", direction))
                            nextActions.append(("shoot", "W"))



        elif direction == "N" and gameStatus.game.weightedImpostorMap[gameStatus.game.me.y - 1][gameStatus.game.me.x] == int(self.maxWeight / 2):

            # my y becomes  y-1
            if gameStatus.game.serverMap[gameStatus.game.me.y - 1][gameStatus.game.me.x] == "~":
                nextActions.append(("move", direction))

            else:
                for key in gameStatus.game.allies:
                    ally = gameStatus.game.allies.get(key)

                    if ally.y == gameStatus.game.me.y - 1:

                        if ally.x > gameStatus.game.me.x:
                            # muoviti ad nord e spara ad est
                            nextActions.append(("move", direction))
                            nextActions.append(("shoot", "E"))

                        if ally.x < gameStatus.game.me.x:
                            # muoviti a nord e spara ad ovest
                            nextActions.append(("move", direction))
                            nextActions.append(("shoot", "W"))


        # Non sono andato in linea di tiro
        else:
            nextActions.append(("move", direction))
    else:
        nextActions.append(("move", direction))
    return nextActions
