import asyncio
from thread_deneme import task2

class Deneme():

    def __init__(self):
        super().__init__()
        self.ilk()
        print("initialize run")

        asyncio.run(self.main())

    def ilk(self):  
        print('ilk')

    async def main(self):
        task1=asyncio.create_task(self.gorev1())
        task2=asyncio.create_task(self.gorev2())

    async def gorev1(self):
        print("gorev1")
    async def gorev2(self):
        print("gorev2")  

    

Deneme()