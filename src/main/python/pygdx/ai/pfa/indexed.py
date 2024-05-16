from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph as _IndexedHierarchicalGraph
_IndexedHierarchicalGraph = _IndexedHierarchicalGraph
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.ai.pfa.indexed.IndexedGraph as _IndexedGraph
_IndexedGraph = _IndexedGraph
import com.badlogic.gdx.ai.pfa.Graph as _Graph
_Graph = _Graph
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IndexedHierarchicalGraph():
    """com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph"""
 
    @staticmethod
    def _wrap(java_value: _IndexedHierarchicalGraph) -> 'IndexedHierarchicalGraph':
        return IndexedHierarchicalGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexedHierarchicalGraph):
        """
        Dynamic initializer for IndexedHierarchicalGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexedHierarchicalGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexedHierarchicalGraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph(int)"""
        val = _IndexedHierarchicalGraph(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getLevelCount(self) -> int:
        """public int com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph.getLevelCount()"""
        return int._wrap(super(IndexedHierarchicalGraph, self).getLevelCount())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def getIndex(self, arg0: object):
        """public abstract int com.badlogic.gdx.ai.pfa.indexed.IndexedGraph.getIndex(N)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setLevel(self, arg0: int):
        """public void com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph.setLevel(int)"""
        super(_IndexedHierarchicalGraph, self).setLevel(_int.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph as _IndexedHierarchicalGraph
_IndexedHierarchicalGraph = _IndexedHierarchicalGraph
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.ai.pfa.indexed.IndexedGraph as _IndexedGraph
_IndexedGraph = _IndexedGraph
import com.badlogic.gdx.ai.pfa.Graph as _Graph
_Graph = _Graph
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IndexedHierarchicalGraph():
    """com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph"""
 
    @staticmethod
    def _wrap(java_value: _IndexedHierarchicalGraph) -> 'IndexedHierarchicalGraph':
        return IndexedHierarchicalGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexedHierarchicalGraph):
        """
        Dynamic initializer for IndexedHierarchicalGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexedHierarchicalGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexedHierarchicalGraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph(int)"""
        val = _IndexedHierarchicalGraph(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getLevelCount(self) -> int:
        """public int com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph.getLevelCount()"""
        return int._wrap(super(IndexedHierarchicalGraph, self).getLevelCount())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def getIndex(self, arg0: object):
        """public abstract int com.badlogic.gdx.ai.pfa.indexed.IndexedGraph.getIndex(N)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setLevel(self, arg0: int):
        """public void com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph.setLevel(int)"""
        super(_IndexedHierarchicalGraph, self).setLevel(_int.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.indexed.IndexedHierarchicalGraph 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.indexed.IndexedGraph
import com.badlogic.gdx.ai.pfa.indexed.IndexedGraph as _IndexedGraph
_IndexedGraph = _IndexedGraph
import com.badlogic.gdx.ai.pfa.Graph as _Graph
_Graph = _Graph
from abc import abstractmethod, ABC
 
class IndexedGraph():
    """com.badlogic.gdx.ai.pfa.indexed.IndexedGraph"""
 
    @staticmethod
    def _wrap(java_value: _IndexedGraph) -> 'IndexedGraph':
        return IndexedGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexedGraph):
        """
        Dynamic initializer for IndexedGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexedGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexedGraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder$Metrics
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder as _IndexedAStarPathFinder_Metrics
_Metrics = _IndexedAStarPathFinder_Metrics.Metrics
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Metrics():
    """com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder.Metrics"""
 
    @staticmethod
    def _wrap(java_value: _Metrics) -> 'Metrics':
        return Metrics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Metrics):
        """
        Dynamic initializer for Metrics.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Metrics__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Metrics__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder$Metrics()"""
        val = _Metrics()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder$Metrics()"""
        val = _Metrics()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx.ai import pfa
except ImportError:
    pfa = _import_once("pygdx.ai.pfa")

import com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder as _IndexedAStarPathFinder
_IndexedAStarPathFinder = _IndexedAStarPathFinder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IndexedAStarPathFinder():
    """com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder"""
 
    @staticmethod
    def _wrap(java_value: _IndexedAStarPathFinder) -> 'IndexedAStarPathFinder':
        return IndexedAStarPathFinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexedAStarPathFinder):
        """
        Dynamic initializer for IndexedAStarPathFinder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexedAStarPathFinder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexedAStarPathFinder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def search(self, arg0: 'PathFinderRequest', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder.search(com.badlogic.gdx.ai.pfa.PathFinderRequest<N>,long)"""
        return bool._wrap(super(_IndexedAStarPathFinder, self).search(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'IndexedGraph', arg1: bool):
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder(com.badlogic.gdx.ai.pfa.indexed.IndexedGraph<N>,boolean)"""
        val = _IndexedAStarPathFinder(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def searchConnectionPath(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder.searchConnectionPath(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<com.badlogic.gdx.ai.pfa.Connection<N>>)"""
        return bool._wrap(super(_IndexedAStarPathFinder, self).searchConnectionPath(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def searchNodePath(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder.searchNodePath(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<N>)"""
        return bool._wrap(super(_IndexedAStarPathFinder, self).searchNodePath(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'IndexedGraph'):
        """public com.badlogic.gdx.ai.pfa.indexed.IndexedAStarPathFinder(com.badlogic.gdx.ai.pfa.indexed.IndexedGraph<N>)"""
        val = _IndexedAStarPathFinder(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())