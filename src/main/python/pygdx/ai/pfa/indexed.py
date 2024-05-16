from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.ai.pfa.indexed.IndexedGraph as __IndexedGraph
__IndexedGraph = __IndexedGraph
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.pfa.Graph as __Graph
__Graph = __Graph
 
class IndexedGraph(ABC):
    """com.badlogic.gdx.ai.pfa.indexed.IndexedGraph"""
 
    @staticmethod
    def __wrap(java_value: __IndexedGraph) -> 'IndexedGraph':
        return IndexedGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexedGraph):
        """
        Dynamic initializer for IndexedGraph.
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
    def getNodeCount(self, ):
        """public abstract int com.badlogic.gdx.ai.pfa.indexed.IndexedGraph.getNodeCount()"""
        pass

    @abstractmethod
    def getConnections(self, arg0: object):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.pfa.Connection<N>> com.badlogic.gdx.ai.pfa.Graph.getConnections(N)"""
        pass

    @abstractmethod
    def getIndex(self, arg0: object):
        """public abstract int com.badlogic.gdx.ai.pfa.indexed.IndexedGraph.getIndex(N)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.indexed.IndexedGraph
import com.badlogic.gdx.ai.pfa.indexed.IndexedGraph as __IndexedGraph
__IndexedGraph = __IndexedGraph
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.pfa.Graph as __Graph
__Graph = __Graph
 
class IndexedGraph(ABC):
    """com.badlogic.gdx.ai.pfa.indexed.IndexedGraph"""
 
    @staticmethod
    def __wrap(java_value: __IndexedGraph) -> 'IndexedGraph':
        return IndexedGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexedGraph):
        """
        Dynamic initializer for IndexedGraph.
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
    def getNodeCount(self, ):
        """public abstract int com.badlogic.gdx.ai.pfa.indexed.IndexedGraph.getNodeCount()"""
        pass

    @abstractmethod
    def getConnections(self, arg0: object):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.pfa.Connection<N>> com.badlogic.gdx.ai.pfa.Graph.getConnections(N)"""
        pass

    @abstractmethod
    def getIndex(self, arg0: object):
        """public abstract int com.badlogic.gdx.ai.pfa.indexed.IndexedGraph.getIndex(N)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.indexed.IndexedGraph 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder$Metrics
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
import com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder as __IndexedAStarPathFinder_Metrics
__Metrics = __IndexedAStarPathFinder_Metrics.Metrics
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Metrics():
    """com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder.Metrics"""
 
    @staticmethod
    def __wrap(java_value: __Metrics) -> 'Metrics':
        return Metrics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Metrics):
        """
        Dynamic initializer for Metrics.
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder$Metrics()"""
        val = __Metrics()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def reset(self):
        """public void com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder$Metrics.reset()"""
        super(Metrics, self).reset()

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
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder$Metrics()"""
        val = __Metrics()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder as __IndexedAStarPathFinder
__IndexedAStarPathFinder = __IndexedAStarPathFinder
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import pfa
except ImportError:
    pfa = __import_once__("pygdx.ai.pfa")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IndexedAStarPathFinder():
    """com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder"""
 
    @staticmethod
    def __wrap(java_value: __IndexedAStarPathFinder) -> 'IndexedAStarPathFinder':
        return IndexedAStarPathFinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexedAStarPathFinder):
        """
        Dynamic initializer for IndexedAStarPathFinder.
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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def searchConnectionPath(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder.searchConnectionPath(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<com.badlogic.gdx.ai.pfa.Connection<N>>)"""
        return bool.__wrap(super(__IndexedAStarPathFinder, self).searchConnectionPath(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def search(self, arg0: 'PathFinderRequest', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder.search(com.badlogic.gdx.ai.pfa.PathFinderRequest<N>,long)"""
        return bool.__wrap(super(__IndexedAStarPathFinder, self).search(arg0, __long.valueOf(arg1)))

    @overload
    def searchNodePath(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder.searchNodePath(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<N>)"""
        return bool.__wrap(super(__IndexedAStarPathFinder, self).searchNodePath(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'IndexedGraph', arg1: bool):
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder(com.badlogic.gdx.ai.pfa.indexed.IndexedGraph<N>,boolean)"""
        val = __IndexedAStarPathFinder(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'IndexedGraph'):
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder(com.badlogic.gdx.ai.pfa.indexed.IndexedGraph<N>)"""
        val = __IndexedAStarPathFinder(arg0)
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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph as __IndexedHierarchicalGraph
__IndexedHierarchicalGraph = __IndexedHierarchicalGraph
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.pfa.indexed.IndexedGraph as __IndexedGraph
__IndexedGraph = __IndexedGraph
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import com.badlogic.gdx.ai.pfa.Graph as __Graph
__Graph = __Graph
 
class IndexedHierarchicalGraph(ABC):
    """com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph"""
 
    @staticmethod
    def __wrap(java_value: __IndexedHierarchicalGraph) -> 'IndexedHierarchicalGraph':
        return IndexedHierarchicalGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexedHierarchicalGraph):
        """
        Dynamic initializer for IndexedHierarchicalGraph.
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
    def getLevelCount(self) -> int:
        """public int com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph.getLevelCount()"""
        return int.__wrap(super(IndexedHierarchicalGraph, self).getLevelCount())

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

    @abstractmethod
    def convertNodeBetweenLevels(self, arg0: int, arg1: object, arg2: int):
        """public abstract N com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph.convertNodeBetweenLevels(int,N,int)"""
        pass

    @abstractmethod
    def getConnections(self, arg0: object):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.pfa.Connection<N>> com.badlogic.gdx.ai.pfa.Graph.getConnections(N)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @abstractmethod
    def getIndex(self, arg0: object):
        """public abstract int com.badlogic.gdx.ai.pfa.indexed.IndexedGraph.getIndex(N)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setLevel(self, arg0: int):
        """public void com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph.setLevel(int)"""
        super(__IndexedHierarchicalGraph, self).setLevel(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def getNodeCount(self, ):
        """public abstract int com.badlogic.gdx.ai.pfa.indexed.IndexedGraph.getNodeCount()"""
        pass

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph(int)"""
        val = __IndexedHierarchicalGraph(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))