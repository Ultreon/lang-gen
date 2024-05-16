from __future__ import annotations
from overload import overload


 
import java.util.Spliterator as Spliterator
import com.badlogic.gdx.ai.pfa.SmoothableGraphPath as _SmoothableGraphPath
_SmoothableGraphPath = _SmoothableGraphPath
from pyquantum_helper import override
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import com.badlogic.gdx.ai.pfa.GraphPath as _GraphPath
_GraphPath = _GraphPath
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class SmoothableGraphPath():
    """com.badlogic.gdx.ai.pfa.SmoothableGraphPath"""
 
    @staticmethod
    def _wrap(java_value: _SmoothableGraphPath) -> 'SmoothableGraphPath':
        return SmoothableGraphPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SmoothableGraphPath):
        """
        Dynamic initializer for SmoothableGraphPath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SmoothableGraphPath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SmoothableGraphPath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @abstractmethod
    def truncatePath(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.pfa.SmoothableGraphPath.truncatePath(int)"""
        pass

    @abstractmethod
    def get(self, arg0: int):
        """public abstract N com.badlogic.gdx.ai.pfa.GraphPath.get(int)"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.SmoothableGraphPath
import java.util.Spliterator as Spliterator
import com.badlogic.gdx.ai.pfa.SmoothableGraphPath as _SmoothableGraphPath
_SmoothableGraphPath = _SmoothableGraphPath
from pyquantum_helper import override
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import com.badlogic.gdx.ai.pfa.GraphPath as _GraphPath
_GraphPath = _GraphPath
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class SmoothableGraphPath():
    """com.badlogic.gdx.ai.pfa.SmoothableGraphPath"""
 
    @staticmethod
    def _wrap(java_value: _SmoothableGraphPath) -> 'SmoothableGraphPath':
        return SmoothableGraphPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SmoothableGraphPath):
        """
        Dynamic initializer for SmoothableGraphPath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SmoothableGraphPath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SmoothableGraphPath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @abstractmethod
    def truncatePath(self, arg0: int):
        """public abstract void com.badlogic.gdx.ai.pfa.SmoothableGraphPath.truncatePath(int)"""
        pass

    @abstractmethod
    def get(self, arg0: int):
        """public abstract N com.badlogic.gdx.ai.pfa.GraphPath.get(int)"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.SmoothableGraphPath 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathSmoother
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.pfa.PathSmoother as _PathSmoother
_PathSmoother = _PathSmoother
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PathSmoother():
    """com.badlogic.gdx.ai.pfa.PathSmoother"""
 
    @staticmethod
    def _wrap(java_value: _PathSmoother) -> 'PathSmoother':
        return PathSmoother(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PathSmoother):
        """
        Dynamic initializer for PathSmoother.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PathSmoother__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PathSmoother__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def smoothPath(self, arg0: 'PathSmootherRequest', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathSmoother.smoothPath(com.badlogic.gdx.ai.pfa.PathSmootherRequest<N, V>,long)"""
        return bool._wrap(super(_PathSmoother, self).smoothPath(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'RaycastCollisionDetector'):
        """public com.badlogic.gdx.ai.pfa.PathSmoother(com.badlogic.gdx.ai.utils.RaycastCollisionDetector<V>)"""
        val = _PathSmoother(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def smoothPath(self, arg0: 'SmoothableGraphPath') -> int:
        """public int com.badlogic.gdx.ai.pfa.PathSmoother.smoothPath(com.badlogic.gdx.ai.pfa.SmoothableGraphPath<N, V>)"""
        return int._wrap(super(_PathSmoother, self).smoothPath(arg0))

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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.HierarchicalGraph
import com.badlogic.gdx.ai.pfa.Graph as _Graph
_Graph = _Graph
import com.badlogic.gdx.ai.pfa.HierarchicalGraph as _HierarchicalGraph
_HierarchicalGraph = _HierarchicalGraph
from abc import abstractmethod, ABC
 
class HierarchicalGraph():
    """com.badlogic.gdx.ai.pfa.HierarchicalGraph"""
 
    @staticmethod
    def _wrap(java_value: _HierarchicalGraph) -> 'HierarchicalGraph':
        return HierarchicalGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HierarchicalGraph):
        """
        Dynamic initializer for HierarchicalGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HierarchicalGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HierarchicalGraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathFinderRequestControl
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.pfa.PathFinderRequestControl as _PathFinderRequestControl
_PathFinderRequestControl = _PathFinderRequestControl
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PathFinderRequestControl():
    """com.badlogic.gdx.ai.pfa.PathFinderRequestControl"""
 
    @staticmethod
    def _wrap(java_value: _PathFinderRequestControl) -> 'PathFinderRequestControl':
        return PathFinderRequestControl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PathFinderRequestControl):
        """
        Dynamic initializer for PathFinderRequestControl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PathFinderRequestControl__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PathFinderRequestControl__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequestControl()"""
        val = _PathFinderRequestControl()
        self.__wrapper = val

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

    @overload
    def execute(self, arg0: 'PathFinderRequest') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathFinderRequestControl.execute(com.badlogic.gdx.ai.pfa.PathFinderRequest<N>)"""
        return bool._wrap(super(_PathFinderRequestControl, self).execute(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequestControl()"""
        val = _PathFinderRequestControl()
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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathFinderQueue
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pygdx.ai import msg
except ImportError:
    msg = _import_once("pygdx.ai.msg")

import java.lang.Integer as _int
import com.badlogic.gdx.ai.pfa.PathFinderQueue as _PathFinderQueue
_PathFinderQueue = _PathFinderQueue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PathFinderQueue():
    """com.badlogic.gdx.ai.pfa.PathFinderQueue"""
 
    @staticmethod
    def _wrap(java_value: _PathFinderQueue) -> 'PathFinderQueue':
        return PathFinderQueue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PathFinderQueue):
        """
        Dynamic initializer for PathFinderQueue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PathFinderQueue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PathFinderQueue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'PathFinder'):
        """public com.badlogic.gdx.ai.pfa.PathFinderQueue(com.badlogic.gdx.ai.pfa.PathFinder<N>)"""
        val = _PathFinderQueue(arg0)
        self.__wrapper = val

    @override
    @overload
    def run(self, arg0: int):
        """public void com.badlogic.gdx.ai.pfa.PathFinderQueue.run(long)"""
        super(_PathFinderQueue, self).run(_long.valueOf(arg0))

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

    @overload
    def handleMessage(self, arg0: 'Telegram') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathFinderQueue.handleMessage(com.badlogic.gdx.ai.msg.Telegram)"""
        return bool._wrap(super(_PathFinderQueue, self).handleMessage(arg0))

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
    def size(self) -> int:
        """public int com.badlogic.gdx.ai.pfa.PathFinderQueue.size()"""
        return int._wrap(super(PathFinderQueue, self).size())

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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.Graph
import com.badlogic.gdx.ai.pfa.Graph as _Graph
_Graph = _Graph
from abc import abstractmethod, ABC
 
class Graph():
    """com.badlogic.gdx.ai.pfa.Graph"""
 
    @staticmethod
    def _wrap(java_value: _Graph) -> 'Graph':
        return Graph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Graph):
        """
        Dynamic initializer for Graph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Graph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Graph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getConnections(self, arg0: object):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.pfa.Connection<N>> com.badlogic.gdx.ai.pfa.Graph.getConnections(N)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.DefaultGraphPath
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.ai.pfa.DefaultGraphPath as _DefaultGraphPath
_DefaultGraphPath = _DefaultGraphPath
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultGraphPath():
    """com.badlogic.gdx.ai.pfa.DefaultGraphPath"""
 
    @staticmethod
    def _wrap(java_value: _DefaultGraphPath) -> 'DefaultGraphPath':
        return DefaultGraphPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultGraphPath):
        """
        Dynamic initializer for DefaultGraphPath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultGraphPath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultGraphPath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.pfa.DefaultGraphPath()"""
        val = _DefaultGraphPath()
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.pfa.DefaultGraphPath(com.badlogic.gdx.utils.Array<N>)"""
        val = _DefaultGraphPath(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.pfa.DefaultGraphPath()"""
        val = _DefaultGraphPath()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.pfa.DefaultGraphPath(int)"""
        val = _DefaultGraphPath(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<N> com.badlogic.gdx.ai.pfa.DefaultGraphPath.iterator()"""
        return 'Iterator'._wrap(super(DefaultGraphPath, self).iterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getCount(self) -> int:
        """public int com.badlogic.gdx.ai.pfa.DefaultGraphPath.getCount()"""
        return int._wrap(super(DefaultGraphPath, self).getCount())

    @overload
    def get(self, arg0: int) -> object:
        """public N com.badlogic.gdx.ai.pfa.DefaultGraphPath.get(int)"""
        return object._wrap(super(_DefaultGraphPath, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def reverse(self):
        """public void com.badlogic.gdx.ai.pfa.DefaultGraphPath.reverse()"""
        super(DefaultGraphPath, self).reverse()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.pfa.DefaultGraphPath.clear()"""
        super(DefaultGraphPath, self).clear()

    @override
    @overload
    def add(self, arg0: object):
        """public void com.badlogic.gdx.ai.pfa.DefaultGraphPath.add(N)"""
        super(_DefaultGraphPath, self).add(arg0)

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.DefaultConnection
import com.badlogic.gdx.ai.pfa.DefaultConnection as _DefaultConnection
_DefaultConnection = _DefaultConnection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultConnection():
    """com.badlogic.gdx.ai.pfa.DefaultConnection"""
 
    @staticmethod
    def _wrap(java_value: _DefaultConnection) -> 'DefaultConnection':
        return DefaultConnection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultConnection):
        """
        Dynamic initializer for DefaultConnection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultConnection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultConnection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getCost(self) -> float:
        """public float com.badlogic.gdx.ai.pfa.DefaultConnection.getCost()"""
        return float._wrap(super(DefaultConnection, self).getCost())

    @override
    @overload
    def getToNode(self) -> object:
        """public N com.badlogic.gdx.ai.pfa.DefaultConnection.getToNode()"""
        return object._wrap(super(DefaultConnection, self).getToNode())

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getFromNode(self) -> object:
        """public N com.badlogic.gdx.ai.pfa.DefaultConnection.getFromNode()"""
        return object._wrap(super(DefaultConnection, self).getFromNode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public com.badlogic.gdx.ai.pfa.DefaultConnection(N,N)"""
        val = _DefaultConnection(arg0, arg1)
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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathFinder
import com.badlogic.gdx.ai.pfa.PathFinder as _PathFinder
_PathFinder = _PathFinder
from abc import abstractmethod, ABC
 
class PathFinder():
    """com.badlogic.gdx.ai.pfa.PathFinder"""
 
    @staticmethod
    def _wrap(java_value: _PathFinder) -> 'PathFinder':
        return PathFinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PathFinder):
        """
        Dynamic initializer for PathFinder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PathFinder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PathFinder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.Connection
import com.badlogic.gdx.ai.pfa.Connection as _Connection
_Connection = _Connection
from abc import abstractmethod, ABC
 
class Connection():
    """com.badlogic.gdx.ai.pfa.Connection"""
 
    @staticmethod
    def _wrap(java_value: _Connection) -> 'Connection':
        return Connection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Connection):
        """
        Dynamic initializer for Connection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Connection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Connection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.Heuristic
import com.badlogic.gdx.ai.pfa.Heuristic as _Heuristic
_Heuristic = _Heuristic
from abc import abstractmethod, ABC
 
class Heuristic():
    """com.badlogic.gdx.ai.pfa.Heuristic"""
 
    @staticmethod
    def _wrap(java_value: _Heuristic) -> 'Heuristic':
        return Heuristic(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Heuristic):
        """
        Dynamic initializer for Heuristic.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Heuristic__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Heuristic__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def estimate(self, arg0: object, arg1: object):
        """public abstract float com.badlogic.gdx.ai.pfa.Heuristic.estimate(N,N)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.GraphPath
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import com.badlogic.gdx.ai.pfa.GraphPath as _GraphPath
_GraphPath = _GraphPath
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class GraphPath():
    """com.badlogic.gdx.ai.pfa.GraphPath"""
 
    @staticmethod
    def _wrap(java_value: _GraphPath) -> 'GraphPath':
        return GraphPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GraphPath):
        """
        Dynamic initializer for GraphPath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GraphPath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GraphPath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @abstractmethod
    def get(self, arg0: int):
        """public abstract N com.badlogic.gdx.ai.pfa.GraphPath.get(int)"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: com.badlogic.gdx.ai.pfa.HierarchicalPathFinder
import com.badlogic.gdx.ai.pfa.HierarchicalPathFinder as _HierarchicalPathFinder
_HierarchicalPathFinder = _HierarchicalPathFinder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HierarchicalPathFinder():
    """com.badlogic.gdx.ai.pfa.HierarchicalPathFinder"""
 
    @staticmethod
    def _wrap(java_value: _HierarchicalPathFinder) -> 'HierarchicalPathFinder':
        return HierarchicalPathFinder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HierarchicalPathFinder):
        """
        Dynamic initializer for HierarchicalPathFinder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HierarchicalPathFinder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HierarchicalPathFinder__wrapper":
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
    def searchNodePath(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.HierarchicalPathFinder.searchNodePath(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<N>)"""
        return bool._wrap(super(_HierarchicalPathFinder, self).searchNodePath(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'HierarchicalGraph', arg1: 'PathFinder'):
        """public com.badlogic.gdx.ai.pfa.HierarchicalPathFinder(com.badlogic.gdx.ai.pfa.HierarchicalGraph<N>,com.badlogic.gdx.ai.pfa.PathFinder<N>)"""
        val = _HierarchicalPathFinder(arg0, arg1)
        self.__wrapper = val

    @overload
    def search(self, arg0: 'PathFinderRequest', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.HierarchicalPathFinder.search(com.badlogic.gdx.ai.pfa.PathFinderRequest<N>,long)"""
        return bool._wrap(super(_HierarchicalPathFinder, self).search(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def searchConnectionPath(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath') -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.HierarchicalPathFinder.searchConnectionPath(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<com.badlogic.gdx.ai.pfa.Connection<N>>)"""
        return bool._wrap(super(_HierarchicalPathFinder, self).searchConnectionPath(arg0, arg1, arg2, arg3))

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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathSmootherRequest
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import com.badlogic.gdx.ai.pfa.PathSmootherRequest as _PathSmootherRequest
_PathSmootherRequest = _PathSmootherRequest
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PathSmootherRequest():
    """com.badlogic.gdx.ai.pfa.PathSmootherRequest"""
 
    @staticmethod
    def _wrap(java_value: _PathSmootherRequest) -> 'PathSmootherRequest':
        return PathSmootherRequest(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PathSmootherRequest):
        """
        Dynamic initializer for PathSmootherRequest.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PathSmootherRequest__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PathSmootherRequest__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def refresh(self, arg0: 'SmoothableGraphPath'):
        """public void com.badlogic.gdx.ai.pfa.PathSmootherRequest.refresh(com.badlogic.gdx.ai.pfa.SmoothableGraphPath<N, V>)"""
        super(_PathSmootherRequest, self).refresh(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.pfa.PathSmootherRequest()"""
        val = _PathSmootherRequest()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.pfa.PathSmootherRequest()"""
        val = _PathSmootherRequest()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.ai.pfa.PathFinderRequest
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.pfa.PathFinderRequest as _PathFinderRequest
_PathFinderRequest = _PathFinderRequest
import java.lang.String as _String
_String = _String
try:
    from pygdx.ai import msg
except ImportError:
    msg = _import_once("pygdx.ai.msg")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PathFinderRequest():
    """com.badlogic.gdx.ai.pfa.PathFinderRequest"""
 
    @staticmethod
    def _wrap(java_value: _PathFinderRequest) -> 'PathFinderRequest':
        return PathFinderRequest(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PathFinderRequest):
        """
        Dynamic initializer for PathFinderRequest.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PathFinderRequest__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PathFinderRequest__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def changeStatus(self, arg0: int):
        """public void com.badlogic.gdx.ai.pfa.PathFinderRequest.changeStatus(int)"""
        super(_PathFinderRequest, self).changeStatus(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath', arg4: 'MessageDispatcher'):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequest(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<N>,com.badlogic.gdx.ai.msg.MessageDispatcher)"""
        val = _PathFinderRequest(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'Heuristic', arg3: 'GraphPath'):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequest(N,N,com.badlogic.gdx.ai.pfa.Heuristic<N>,com.badlogic.gdx.ai.pfa.GraphPath<N>)"""
        val = _PathFinderRequest(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def initializeSearch(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathFinderRequest.initializeSearch(long)"""
        return bool._wrap(super(_PathFinderRequest, self).initializeSearch(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def finalizeSearch(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathFinderRequest.finalizeSearch(long)"""
        return bool._wrap(super(_PathFinderRequest, self).finalizeSearch(_long.valueOf(arg0)))

    @overload
    def search(self, arg0: 'PathFinder', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.ai.pfa.PathFinderRequest.search(com.badlogic.gdx.ai.pfa.PathFinder<N>,long)"""
        return bool._wrap(super(_PathFinderRequest, self).search(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequest()"""
        val = _PathFinderRequest()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.pfa.PathFinderRequest()"""
        val = _PathFinderRequest()
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