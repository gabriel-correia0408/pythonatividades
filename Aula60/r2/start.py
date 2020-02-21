
from Aula60.r2.viagem import  Viagem
from Aula60.r2.terminal import Terminal
from Aula60.r2.aviao import Aviao


Viagem('policial','presidiario', Terminal, Aviao)
Viagem('policial','', Aviao, Terminal)
Viagem('piloto','policial', Terminal, Aviao)
Viagem('piloto','', Aviao, Terminal)
Viagem('piloto','oficial1', Terminal, Aviao)
Viagem('piloto','', Aviao, Terminal)
Viagem('piloto','oficial2', Terminal, Aviao)
Viagem('piloto','', Aviao, Terminal)
Viagem('chefe de serviço','piloto', Terminal, Aviao)
Viagem('chefe de serviço','', Aviao, Terminal)
Viagem('chefe de serviço','comissário1', Terminal, Aviao)
Viagem('chefe de serviço','', Aviao, Terminal)
Viagem('chefe de serviço','comissário2', Terminal, Aviao)