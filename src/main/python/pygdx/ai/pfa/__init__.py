from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.ai.pfa.Connection as __Connection
__Connection = __Connection
from abc import abstractmethod, ABC
 
class Connection(ABC):
    """com.badlogic.gdx.ai.pfa.Connection"""
 
    @staticmethod
    def __wrap(java_value: __Connection) -> 'Connection':
        return Connection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Connection):
        """
        Dynamic initializer for Connection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getCost(self, ):
        """public abstract float com.badlogic.gdx.ai.pfa.Connection.getCost()"""
        pass

    @abstractmethod
    def getFromNode(self, ):
        """public abstract N com.badlogic.gdx.ai.pfa.Connection.getFromNode()"""
        pass

    @abstractmethod
    def getToNode(self, ):
        """public abstract N com.badlogic.gdx.ai.pfa.Connection.getToNode()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.Connection
import com.badlogic.gdx.ai.pfa.Connection as __Connection
__Connection = __Connection
from abc import abstractmethod, ABC
 
class Connection(ABC):
    """com.badlogic.gdx.ai.pfa.Connection"""
 
    @staticmethod
    def __wrap(java_value: __Connection) -> 'Connection':
        return Connection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Connection):
        """
        Dynamic initializer for Connection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getCost(self, ):
        """public abstract float com.badlogic.gdx.ai.pfa.Connection.getCost()"""
        pass

    @abstractmethod
    def getFromNode(self, ):
        """public abstract N com.badlogic.gdx.ai.pfa.Connection.getFromNode()"""
        pass

    @abstractmethod
    def getToNode(self, ):
        """public abstract N com.badlogic.gdx.ai.pfa.Connection.getToNode()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.Connection 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.DefaultConnection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.pfa.DefaultConnection as __DefaultConnection
__DefaultConnection = __DefaultConnection
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DefaultConnection(__Connection, Connection):
    """com.badlogic.gdx.ai.pfa.DefaultConnection"""
 
    @staticmethod
    def __wrap(java_value: __DefaultConnection) -> 'DefaultConnection':
        return DefaultConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultConnection):
        """
        Dynamic initializer for DefaultConnection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getCost(self) -> float:
        """public float com.badlogic.gdx.ai.pfa.DefaultConnection.getCost()"""
        return float.__wrap(super(DefaultConnection, self).getCost())

    @override
    @overload
    def getToNode(self) -> object:
        """public N com.badlogic.gdx.ai.pfa.DefaultConnection.getToNode()"""
        return object.__wrap(super(DefaultConnection, self).getToNode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getFromNode(self) -> object:
        """public N com.badlogic.gdx.ai.pfa.DefaultConnection.getFromNode()"""
        return object.__wrap(super(DefaultConnection, self).getFromNode())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public com.badlogic.gdx.ai.pfa.DefaultConnection(N,N)"""
        val = __DefaultConnection(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathFinder
import com.badlogic.gdx.ai.pfa.PathFinder as __PathFinder
__PathFinder = __PathFinder
from abc import abstractmethod, ABC
 
class PathFinder(ABC):
    """com.badlogic.gdx.ai.pfa.PathFinder"""
 
    @staticmethod
    def __wrap(java_value: __PathFinder) -> 'PathFinder':
        return PathFinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PathFinder):
        """
        Dynamic initializer for PathFinder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def search(self, arg0: 'PathFinderRequest', arg1: int):
        """public abstract boolean com.badlogic.gdx.ai.pfa.PathFinder.search(com.badlogic.gdx.ai.pfa.PathFinderRequest<N>,long)"""
        pass

    @abstractmethod
    def searchNodePath(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath'):
        """public abstract boolean com.badlogic.gdx.ai.pfa.PathFinder.searchNodePath(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<N>)"""
        pass

    @abstractmethod
    def searchConnectionPath(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath'):
        """public abstract boolean com.badlogic.gdx.ai.pfa.PathFinder.searchConnectionPath(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<com.badlogic.gdx.ai.pfa.Connection<N>>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.HierarchicalGraph
import com.badlogic.gdx.ai.pfa.HierarchicalGraph as __HierarchicalGraph
__HierarchicalGraph = __HierarchicalGraph
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.pfa.Graph as __Graph
__Graph = __Graph
 
class HierarchicalGraph(ABC, __Graph, Graph):
    """com.badlogic.gdx.ai.pfa.HierarchicalGraph"""
 
    @staticmethod
    def __wrap(java_value: __HierarchicalGraph) -> 'HierarchicalGraph':
        return HierarchicalGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HierarchicalGraph):
        """
        Dynamic initializer for HierarchicalGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getLevelCount(self, ):
        """public abstract int com.badlogic.gdx.ai.pfa.HierarchicalGraph.getLevelCount()"""
        pass

    @abstractmethod
    def setLevel(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.pfa.HierarchicalGraph.setLevel(int)"""
        pass

    @abstractmethod
    def convertNodeBetweenLevels(self, arg0: int, arg1: object, arg2: int):
        """public abstract N com.badlogic.gdx.ai.pfa.HierarchicalGraph.convertNodeBetweenLevels(int,N,int)"""
        pass

    @abstractmethod
    def getConnections(self, arg0: object):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.pfa.Connection<N>> com.badlogic.gdx.ai.pfa.Graph.getConnections(N)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathFinderRequest
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.pfa.PathFinderRequest as __PathFinderRequest
__PathFinderRequest = __PathFinderRequest
try:
    from pygdx.ai import msg
except ImportError:
    msg = __import_once__("pygdx.ai.msg")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PathFinderRequest():
    """com.badlogic.gdx.ai.pfa.PathFinderRequest"""
 
    @staticmethod
    def __wrap(java_value: __PathFinderRequest) -> 'PathFinderRequest':
        return PathFinderRequest(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PathFinderRequest):
        """
        Dynamic initializer for PathFinderRequest.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequest()"""
        val = __PathFinderRequest()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def search(self, arg0: 'PathFinder', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathFinderRequest.search(com.badlogic.gdx.ai.pfa.PathFinder<N>,long)"""
        return bool.__wrap(super(__PathFinderRequest, self).search(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath'):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequest(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<N>)"""
        val = __PathFinderRequest(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def changeStatus(self, arg0: int):
        """public void com.badlogic.gdx.ai.pfa.PathFinderRequest.changeStatus(int)"""
        super(__PathFinderRequest, self).changeStatus(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequest()"""
        val = __PathFinderRequest()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def finalizeSearch(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathFinderRequest.finalizeSearch(long)"""
        return bool.__wrap(super(__PathFinderRequest, self).finalizeSearch(__long.valueOf(arg0)))

    @overload
    def initializeSearch(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathFinderRequest.initializeSearch(long)"""
        return bool.__wrap(super(__PathFinderRequest, self).initializeSearch(__long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath', arg4: 'MessageDispatcher'):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequest(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<N>,com.badlogic.gdx.ai.msg.MessageDispatcher)"""
        val = __PathFinderRequest(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathFinderQueue
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.ai import msg
except ImportError:
    msg = __import_once__("pygdx.ai.msg")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.pfa.PathFinderQueue as __PathFinderQueue
__PathFinderQueue = __PathFinderQueue
from builtins import int
 
class PathFinderQueue(ai.__Schedulable, sched.Schedulable, ai.__Telegraph, msg.Telegraph):
    """com.badlogic.gdx.ai.pfa.PathFinderQueue"""
 
    @staticmethod
    def __wrap(java_value: __PathFinderQueue) -> 'PathFinderQueue':
        return PathFinderQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PathFinderQueue):
        """
        Dynamic initializer for PathFinderQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'PathFinder'):
        """public com.badlogic.gdx.ai.pfa.PathFinderQueue(com.badlogic.gdx.ai.pfa.PathFinder<N>)"""
        val = __PathFinderQueue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.ai.pfa.PathFinderQueue.size()"""
        return int.__wrap(super(PathFinderQueue, self).size())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def handleMessage(self, arg0: 'Telegram') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathFinderQueue.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        return bool.__wrap(super(__PathFinderQueue, self).handleMessage(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def run(self, arg0: int):
        """public void com.badlogic.gdx.ai.pfa.PathFinderQueue.run(long)"""
        super(__PathFinderQueue, self).run(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.GraphPath
import java.util.Spliterator as Spliterator
import com.badlogic.gdx.ai.pfa.GraphPath as __GraphPath
__GraphPath = __GraphPath
from abc import abstractmethod, ABC
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
 
class GraphPath(ABC, __Iterable, Iterable):
    """com.badlogic.gdx.ai.pfa.GraphPath"""
 
    @staticmethod
    def __wrap(java_value: __GraphPath) -> 'GraphPath':
        return GraphPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GraphPath):
        """
        Dynamic initializer for GraphPath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def reverse(self, ):
        """public abstract void com.badlogic.gdx.ai.pfa.GraphPath.reverse()"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract void com.badlogic.gdx.ai.pfa.GraphPath.add(N)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void com.badlogic.gdx.ai.pfa.GraphPath.clear()"""
        pass

    @abstractmethod
    def getCount(self, ):
        """public abstract int com.badlogic.gdx.ai.pfa.GraphPath.getCount()"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<T> java.lang.Iterable.iterator()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @abstractmethod
    def get(self, arg0: int):
        """public abstract N com.badlogic.gdx.ai.pfa.GraphPath.get(int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.Graph
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.pfa.Graph as __Graph
__Graph = __Graph
 
class Graph(ABC):
    """com.badlogic.gdx.ai.pfa.Graph"""
 
    @staticmethod
    def __wrap(java_value: __Graph) -> 'Graph':
        return Graph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Graph):
        """
        Dynamic initializer for Graph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getConnections(self, arg0: object):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.pfa.Connection<N>> com.badlogic.gdx.ai.pfa.Graph.getConnections(N)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.SmoothableGraphPath
import com.badlogic.gdx.ai.pfa.SmoothableGraphPath as __SmoothableGraphPath
__SmoothableGraphPath = __SmoothableGraphPath
import java.util.Spliterator as Spliterator
import com.badlogic.gdx.ai.pfa.GraphPath as __GraphPath
__GraphPath = __GraphPath
from abc import abstractmethod, ABC
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
 
class SmoothableGraphPath(ABC, __GraphPath, GraphPath):
    """com.badlogic.gdx.ai.pfa.SmoothableGraphPath"""
 
    @staticmethod
    def __wrap(java_value: __SmoothableGraphPath) -> 'SmoothableGraphPath':
        return SmoothableGraphPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SmoothableGraphPath):
        """
        Dynamic initializer for SmoothableGraphPath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getNodePosition(self, arg0: int):
        """public abstract V com.badlogic.gdx.ai.pfa.SmoothableGraphPath.getNodePosition(int)"""
        pass

    @abstractmethod
    def reverse(self, ):
        """public abstract void com.badlogic.gdx.ai.pfa.GraphPath.reverse()"""
        pass

    @abstractmethod
    def add(self, arg0: object):
        """public abstract void com.badlogic.gdx.ai.pfa.GraphPath.add(N)"""
        pass

    @abstractmethod
    def swapNodes(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.ai.pfa.SmoothableGraphPath.swapNodes(int,int)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void com.badlogic.gdx.ai.pfa.GraphPath.clear()"""
        pass

    @abstractmethod
    def getCount(self, ):
        """public abstract int com.badlogic.gdx.ai.pfa.GraphPath.getCount()"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<T> java.lang.Iterable.iterator()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @abstractmethod
    def truncatePath(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.pfa.SmoothableGraphPath.truncatePath(int)"""
        pass

    @abstractmethod
    def get(self, arg0: int):
        """public abstract N com.badlogic.gdx.ai.pfa.GraphPath.get(int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.DefaultGraphPath
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.pfa.DefaultGraphPath as __DefaultGraphPath
__DefaultGraphPath = __DefaultGraphPath
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class DefaultGraphPath(__GraphPath, GraphPath):
    """com.badlogic.gdx.ai.pfa.DefaultGraphPath"""
 
    @staticmethod
    def __wrap(java_value: __DefaultGraphPath) -> 'DefaultGraphPath':
        return DefaultGraphPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultGraphPath):
        """
        Dynamic initializer for DefaultGraphPath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.pfa.DefaultGraphPath()"""
        val = __DefaultGraphPath()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<N> com.badlogic.gdx.ai.pfa.DefaultGraphPath.iterator()"""
        return 'Iterator'.__wrap(super(DefaultGraphPath, self).iterator())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.pfa.DefaultGraphPath(int)"""
        val = __DefaultGraphPath(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getCount(self) -> int:
        """public int com.badlogic.gdx.ai.pfa.DefaultGraphPath.getCount()"""
        return int.__wrap(super(DefaultGraphPath, self).getCount())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.ai.pfa.DefaultGraphPath.add(N)"""
        super(__DefaultGraphPath, self).add(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.pfa.DefaultGraphPath(com.badlogic.gdx.utils.Array<N>)"""
        val = __DefaultGraphPath(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def reverse(self):
        """public void com.badlogic.gdx.ai.pfa.DefaultGraphPath.reverse()"""
        super(DefaultGraphPath, self).reverse()

    @overload
    def get(self, arg0: int) -> object:
        """public N com.badlogic.gdx.ai.pfa.DefaultGraphPath.get(int)"""
        return object.__wrap(super(__DefaultGraphPath, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.pfa.DefaultGraphPath.clear()"""
        super(DefaultGraphPath, self).clear()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.pfa.DefaultGraphPath()"""
        val = __DefaultGraphPath()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.HierarchicalPathFinder
import com.badlogic.gdx.ai.pfa.HierarchicalPathFinder as __HierarchicalPathFinder
__HierarchicalPathFinder = __HierarchicalPathFinder
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HierarchicalPathFinder(__PathFinder, PathFinder):
    """com.badlogic.gdx.ai.pfa.HierarchicalPathFinder"""
 
    @staticmethod
    def __wrap(java_value: __HierarchicalPathFinder) -> 'HierarchicalPathFinder':
        return HierarchicalPathFinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HierarchicalPathFinder):
        """
        Dynamic initializer for HierarchicalPathFinder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'HierarchicalGraph', arg1: 'PathFinder'):
        """public com.badlogic.gdx.ai.pfa.HierarchicalPathFinder(com.badlogic.gdx.ai.pfa.HierarchicalGraph<N>,com.badlogic.gdx.ai.pfa.PathFinder<N>)"""
        val = __HierarchicalPathFinder(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def searchConnectionPath(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.HierarchicalPathFinder.searchConnectionPath(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<com.badlogic.gdx.ai.pfa.Connection<N>>)"""
        return bool.__wrap(super(__HierarchicalPathFinder, self).searchConnectionPath(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def searchNodePath(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.HierarchicalPathFinder.searchNodePath(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<N>)"""
        return bool.__wrap(super(__HierarchicalPathFinder, self).searchNodePath(arg0, arg1, arg2, arg3))

    @overload
    def search(self, arg0: 'PathFinderRequest', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.HierarchicalPathFinder.search(com.badlogic.gdx.ai.pfa.PathFinderRequest<N>,long)"""
        return bool.__wrap(super(__HierarchicalPathFinder, self).search(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathFinderRequestControl
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.pfa.PathFinderRequestControl as __PathFinderRequestControl
__PathFinderRequestControl = __PathFinderRequestControl
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PathFinderRequestControl():
    """com.badlogic.gdx.ai.pfa.PathFinderRequestControl"""
 
    @staticmethod
    def __wrap(java_value: __PathFinderRequestControl) -> 'PathFinderRequestControl':
        return PathFinderRequestControl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PathFinderRequestControl):
        """
        Dynamic initializer for PathFinderRequestControl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequestControl()"""
        val = __PathFinderRequestControl()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def execute(self, arg0: 'PathFinderRequest') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathFinderRequestControl.execute(com.badlogic.gdx.ai.pfa.PathFinderRequest<N>)"""
        return bool.__wrap(super(__PathFinderRequestControl, self).execute(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequestControl()"""
        val = __PathFinderRequestControl()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.Heuristic
import com.badlogic.gdx.ai.pfa.Heuristic as __Heuristic
__Heuristic = __Heuristic
from abc import abstractmethod, ABC
 
class Heuristic(ABC):
    """com.badlogic.gdx.ai.pfa.Heuristic"""
 
    @staticmethod
    def __wrap(java_value: __Heuristic) -> 'Heuristic':
        return Heuristic(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Heuristic):
        """
        Dynamic initializer for Heuristic.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def estimate(self, arg0: object, arg1: object):
        """public abstract float com.badlogic.gdx.ai.pfa.Heuristic.estimate(N,N)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathSmoother
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.ai.pfa.PathSmoother as __PathSmoother
__PathSmoother = __PathSmoother
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

from builtins import int
 
class PathSmoother():
    """com.badlogic.gdx.ai.pfa.PathSmoother"""
 
    @staticmethod
    def __wrap(java_value: __PathSmoother) -> 'PathSmoother':
        return PathSmoother(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PathSmoother):
        """
        Dynamic initializer for PathSmoother.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'RaycastCollisionDetector'):
        """public com.badlogic.gdx.ai.pfa.PathSmoother(com.badlogic.gdx.ai.utils.RaycastCollisionDetector<V>)"""
        val = __PathSmoother(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def smoothPath(self, arg0: 'PathSmootherRequest', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathSmoother.smoothPath(com.badlogic.gdx.ai.pfa.PathSmootherRequest<N, V>,long)"""
        return bool.__wrap(super(__PathSmoother, self).smoothPath(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def smoothPath(self, arg0: 'SmoothableGraphPath') -> int:
        """public int com.badlogic.gdx.ai.pfa.PathSmoother.smoothPath(com.badlogic.gdx.ai.pfa.SmoothableGraphPath<N, V>)"""
        return int.__wrap(super(__PathSmoother, self).smoothPath(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathSmootherRequest
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.pfa.PathSmootherRequest as __PathSmootherRequest
__PathSmootherRequest = __PathSmootherRequest
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PathSmootherRequest():
    """com.badlogic.gdx.ai.pfa.PathSmootherRequest"""
 
    @staticmethod
    def __wrap(java_value: __PathSmootherRequest) -> 'PathSmootherRequest':
        return PathSmootherRequest(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PathSmootherRequest):
        """
        Dynamic initializer for PathSmootherRequest.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def refresh(self, arg0: 'SmoothableGraphPath'):
        """public void com.badlogic.gdx.ai.pfa.PathSmootherRequest.refresh(com.badlogic.gdx.ai.pfa.SmoothableGraphPath<N, V>)"""
        super(__PathSmootherRequest, self).refresh(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.pfa.PathSmootherRequest()"""
        val = __PathSmootherRequest()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.pfa.PathSmootherRequest()"""
        val = __PathSmootherRequest()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))