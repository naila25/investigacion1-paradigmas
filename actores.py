import asyncio

#aqui definimos un Actor genérico
class Actor:
    def __init__(self, name, inbox):
        # cada actor tiene un nombre y un buzón 
        self.name = name
        self.inbox = inbox  # Cola de mensajes

#funcion para enviar mensaje a otro actor
    async def send(self, message, other_actor):
        await other_actor.inbox.put(message)

#función para recibir mensaje 
    async def receive(self):
        message = await self.inbox.get()
        return message


async def main():
    # Creamos dos colas para los actores (cada actor tiene su buzón)
    inbox1 = asyncio.Queue()
    inbox2 = asyncio.Queue()

    # Creamos los actores
    actor1 = Actor("Actor1", inbox1)
    actor2 = Actor("Actor2", inbox2)

    print("Escribe mensajes entre Actor1 y Actor2 (escribe 'salir' para terminar)\n")

    while True:
        # Actor1 envía mensaje a Actor2
        msg1 = input("Actor1: ")
        await actor1.send(msg1, actor2) # se envia al buzon de actor2

        if msg1.lower() == "salir":
            print("Fin de la conversación.")
            break

        # Actor2 recibe mensaje del actor1
        recibido1 = await actor2.receive()
        print(f"Actor2 recibió: {recibido1}")

        # Actor2 responde a Actor1
        msg2 = input("Actor2: ")
        await actor2.send(msg2, actor1)

        if msg2.lower() == "salir":
            print("Fin de la conversación.")
            break

        # Actor1 recibe mensaje del actor2
        recibido2 = await actor1.receive()
        print(f"Actor1 recibió: {recibido2}")


#Ejecutar el programa
asyncio.run(main()) # asyncio permite que ambos actores puedan enviar y recibir mensajes sin bloquearse