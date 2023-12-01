from Garden import Gardener, TomatoBush, Tomato

Gardener.knowledge_base()

tomato_bush = TomatoBush(5)
gardener = Gardener("Иван", tomato_bush)

gardener.work()
gardener.harvest()
gardener.work()
gardener.work()
gardener.harvest()
gardener.harvest()
gardener.work()



