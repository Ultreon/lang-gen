from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.graph.ValueGraphBuilder as __ValueGraphBuilder
__ValueGraphBuilder = __ValueGraphBuilder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.graph.ImmutableValueGraph as __ImmutableValueGraph_Builder
__Builder = __ImmutableValueGraph_Builder.Builder
import java.lang.String as __String
__String = __String
import com.google.common.graph.MutableValueGraph as __MutableValueGraph
__MutableValueGraph = __MutableValueGraph
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ValueGraphBuilder():
    """com.google.common.graph.ValueGraphBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ValueGraphBuilder) -> 'ValueGraphBuilder':
        return ValueGraphBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueGraphBuilder):
        """
        Dynamic initializer for ValueGraphBuilder.
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
    def build(self) -> 'MutableValueGraph':
        """public <N1 extends N,V1 extends V> com.google.common.graph.MutableValueGraph<N1, V1> com.google.common.graph.ValueGraphBuilder.build()"""
        return 'MutableValueGraph'.__wrap(super(ValueGraphBuilder, self).build())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def allowsSelfLoops(self, allowsSelfLoops: bool) -> 'ValueGraphBuilder':
        """public com.google.common.graph.ValueGraphBuilder<N, V> com.google.common.graph.ValueGraphBuilder.allowsSelfLoops(boolean)"""
        return 'ValueGraphBuilder'.__wrap(super(__ValueGraphBuilder, self).allowsSelfLoops(__boolean.valueOf(allowsSelfLoops)))

    @overload
    def incidentEdgeOrder(self, incidentEdgeOrder: 'ElementOrder') -> 'ValueGraphBuilder':
        """public <N1 extends N> com.google.common.graph.ValueGraphBuilder<N1, V> com.google.common.graph.ValueGraphBuilder.incidentEdgeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'ValueGraphBuilder'.__wrap(super(__ValueGraphBuilder, self).incidentEdgeOrder(incidentEdgeOrder))

    @overload
    def expectedNodeCount(self, expectedNodeCount: int) -> 'ValueGraphBuilder':
        """public com.google.common.graph.ValueGraphBuilder<N, V> com.google.common.graph.ValueGraphBuilder.expectedNodeCount(int)"""
        return 'ValueGraphBuilder'.__wrap(super(__ValueGraphBuilder, self).expectedNodeCount(__int.valueOf(expectedNodeCount)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def directed() -> 'ValueGraphBuilder':
        """public static com.google.common.graph.ValueGraphBuilder<java.lang.Object, java.lang.Object> com.google.common.graph.ValueGraphBuilder.directed()"""
        return ValueGraphBuilder.__wrap(__ValueGraphBuilder.directed())

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

    @staticmethod
    @overload
    def undirected() -> 'ValueGraphBuilder':
        """public static com.google.common.graph.ValueGraphBuilder<java.lang.Object, java.lang.Object> com.google.common.graph.ValueGraphBuilder.undirected()"""
        return ValueGraphBuilder.__wrap(__ValueGraphBuilder.undirected())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def nodeOrder(self, nodeOrder: 'ElementOrder') -> 'ValueGraphBuilder':
        """public <N1 extends N> com.google.common.graph.ValueGraphBuilder<N1, V> com.google.common.graph.ValueGraphBuilder.nodeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'ValueGraphBuilder'.__wrap(super(__ValueGraphBuilder, self).nodeOrder(nodeOrder))

    @overload
    def immutable(self) -> 'Builder':
        """public <N1 extends N,V1 extends V> com.google.common.graph.ImmutableValueGraph$Builder<N1, V1> com.google.common.graph.ValueGraphBuilder.immutable()"""
        return 'Builder'.__wrap(super(ValueGraphBuilder, self).immutable())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def from(graph: 'ValueGraph') -> 'ValueGraphBuilder':
        """public static <N,V> com.google.common.graph.ValueGraphBuilder<N, V> com.google.common.graph.ValueGraphBuilder.from(com.google.common.graph.ValueGraph<N, V>)"""
        return ValueGraphBuilder.__wrap(__ValueGraphBuilder.from(graph))

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

 
 
 
# CLASS: com.google.common.graph.ValueGraphBuilder
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.graph.ValueGraphBuilder as __ValueGraphBuilder
__ValueGraphBuilder = __ValueGraphBuilder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.graph.ImmutableValueGraph as __ImmutableValueGraph_Builder
__Builder = __ImmutableValueGraph_Builder.Builder
import java.lang.String as __String
__String = __String
import com.google.common.graph.MutableValueGraph as __MutableValueGraph
__MutableValueGraph = __MutableValueGraph
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ValueGraphBuilder():
    """com.google.common.graph.ValueGraphBuilder"""
 
    @staticmethod
    def __wrap(java_value: __ValueGraphBuilder) -> 'ValueGraphBuilder':
        return ValueGraphBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueGraphBuilder):
        """
        Dynamic initializer for ValueGraphBuilder.
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
    def build(self) -> 'MutableValueGraph':
        """public <N1 extends N,V1 extends V> com.google.common.graph.MutableValueGraph<N1, V1> com.google.common.graph.ValueGraphBuilder.build()"""
        return 'MutableValueGraph'.__wrap(super(ValueGraphBuilder, self).build())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def allowsSelfLoops(self, allowsSelfLoops: bool) -> 'ValueGraphBuilder':
        """public com.google.common.graph.ValueGraphBuilder<N, V> com.google.common.graph.ValueGraphBuilder.allowsSelfLoops(boolean)"""
        return 'ValueGraphBuilder'.__wrap(super(__ValueGraphBuilder, self).allowsSelfLoops(__boolean.valueOf(allowsSelfLoops)))

    @overload
    def incidentEdgeOrder(self, incidentEdgeOrder: 'ElementOrder') -> 'ValueGraphBuilder':
        """public <N1 extends N> com.google.common.graph.ValueGraphBuilder<N1, V> com.google.common.graph.ValueGraphBuilder.incidentEdgeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'ValueGraphBuilder'.__wrap(super(__ValueGraphBuilder, self).incidentEdgeOrder(incidentEdgeOrder))

    @overload
    def expectedNodeCount(self, expectedNodeCount: int) -> 'ValueGraphBuilder':
        """public com.google.common.graph.ValueGraphBuilder<N, V> com.google.common.graph.ValueGraphBuilder.expectedNodeCount(int)"""
        return 'ValueGraphBuilder'.__wrap(super(__ValueGraphBuilder, self).expectedNodeCount(__int.valueOf(expectedNodeCount)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def directed() -> 'ValueGraphBuilder':
        """public static com.google.common.graph.ValueGraphBuilder<java.lang.Object, java.lang.Object> com.google.common.graph.ValueGraphBuilder.directed()"""
        return ValueGraphBuilder.__wrap(__ValueGraphBuilder.directed())

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

    @staticmethod
    @overload
    def undirected() -> 'ValueGraphBuilder':
        """public static com.google.common.graph.ValueGraphBuilder<java.lang.Object, java.lang.Object> com.google.common.graph.ValueGraphBuilder.undirected()"""
        return ValueGraphBuilder.__wrap(__ValueGraphBuilder.undirected())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def nodeOrder(self, nodeOrder: 'ElementOrder') -> 'ValueGraphBuilder':
        """public <N1 extends N> com.google.common.graph.ValueGraphBuilder<N1, V> com.google.common.graph.ValueGraphBuilder.nodeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'ValueGraphBuilder'.__wrap(super(__ValueGraphBuilder, self).nodeOrder(nodeOrder))

    @overload
    def immutable(self) -> 'Builder':
        """public <N1 extends N,V1 extends V> com.google.common.graph.ImmutableValueGraph$Builder<N1, V1> com.google.common.graph.ValueGraphBuilder.immutable()"""
        return 'Builder'.__wrap(super(ValueGraphBuilder, self).immutable())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def from(graph: 'ValueGraph') -> 'ValueGraphBuilder':
        """public static <N,V> com.google.common.graph.ValueGraphBuilder<N, V> com.google.common.graph.ValueGraphBuilder.from(com.google.common.graph.ValueGraph<N, V>)"""
        return ValueGraphBuilder.__wrap(__ValueGraphBuilder.from(graph))

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

 
 
 
# CLASS: com.google.common.graph.ValueGraphBuilder 
 
 
# CLASS: com.google.common.graph.ImmutableGraph
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.graph.ImmutableGraph as __ImmutableGraph
__ImmutableGraph = __ImmutableGraph
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.graph.ElementOrder as __ElementOrder
__ElementOrder = __ElementOrder
import com.google.common.graph.AbstractGraph as __AbstractGraph
__AbstractGraph = __AbstractGraph
from builtins import int
 
class ImmutableGraph():
    """com.google.common.graph.ImmutableGraph"""
 
    @staticmethod
    def __wrap(java_value: __ImmutableGraph) -> 'ImmutableGraph':
        return ImmutableGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutableGraph):
        """
        Dynamic initializer for ImmutableGraph.
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
 
    @staticmethod
    @overload
    def copyOf(graph: 'Graph') -> 'ImmutableGraph':
        """public static <N> com.google.common.graph.ImmutableGraph<N> com.google.common.graph.ImmutableGraph.copyOf(com.google.common.graph.Graph<N>)"""
        return ImmutableGraph.__wrap(__ImmutableGraph.copyOf(graph))

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
    def incidentEdgeOrder(self) -> 'ElementOrder':
        """public com.google.common.graph.ElementOrder<N> com.google.common.graph.ImmutableGraph.incidentEdgeOrder()"""
        return 'ElementOrder'.__wrap(super(ImmutableGraph, self).incidentEdgeOrder())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractGraph.hashCode()"""
        return int.__wrap(super(AbstractGraph, self).hashCode())

    @staticmethod
    @overload
    def copyOf(graph: 'ImmutableGraph') -> 'ImmutableGraph':
        """public static <N> com.google.common.graph.ImmutableGraph<N> com.google.common.graph.ImmutableGraph.copyOf(com.google.common.graph.ImmutableGraph<N>)"""
        return ImmutableGraph.__wrap(__ImmutableGraph.copyOf(graph))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractGraph.toString()"""
        return str.__wrap(super(AbstractGraph, self).toString())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractGraph.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractGraph, self).equals(obj)) 
 
 
# CLASS: com.google.common.graph.Network
import com.google.common.graph.Network as __Network
__Network = __Network
from abc import abstractmethod, ABC
 
class Network(ABC):
    """com.google.common.graph.Network"""
 
    @staticmethod
    def __wrap(java_value: __Network) -> 'Network':
        return Network(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Network):
        """
        Dynamic initializer for Network.
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
    def incidentNodes(self, edge: object):
        """public abstract com.google.common.graph.EndpointPair<N> com.google.common.graph.Network.incidentNodes(E)"""
        pass

    @abstractmethod
    def adjacentEdges(self, edge: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.adjacentEdges(E)"""
        pass

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.Network.nodes()"""
        pass

    @abstractmethod
    def degree(self, node: object):
        """public abstract int com.google.common.graph.Network.degree(N)"""
        pass

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.adjacentNodes(N)"""
        pass

    @abstractmethod
    def inEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.inEdges(N)"""
        pass

    @abstractmethod
    def allowsParallelEdges(self, ):
        """public abstract boolean com.google.common.graph.Network.allowsParallelEdges()"""
        pass

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.graph.Network.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.Network.allowsSelfLoops()"""
        pass

    @abstractmethod
    def edgeConnecting(self, endpoints: 'EndpointPair'):
        """public abstract java.util.Optional<E> com.google.common.graph.Network.edgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.graph.Network.hashCode()"""
        pass

    @abstractmethod
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.Network.isDirected()"""
        pass

    @abstractmethod
    def asGraph(self, ):
        """public abstract com.google.common.graph.Graph<N> com.google.common.graph.Network.asGraph()"""
        pass

    @abstractmethod
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.Network.nodeOrder()"""
        pass

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.successors(N)"""
        pass

    @abstractmethod
    def inDegree(self, node: object):
        """public abstract int com.google.common.graph.Network.inDegree(N)"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, endpoints: 'EndpointPair'):
        """public abstract boolean com.google.common.graph.Network.hasEdgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def edgeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<E> com.google.common.graph.Network.edgeOrder()"""
        pass

    @abstractmethod
    def edgeConnecting(self, nodeU: object, nodeV: object):
        """public abstract java.util.Optional<E> com.google.common.graph.Network.edgeConnecting(N,N)"""
        pass

    @abstractmethod
    def edgesConnecting(self, endpoints: 'EndpointPair'):
        """public abstract java.util.Set<E> com.google.common.graph.Network.edgesConnecting(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def edgesConnecting(self, nodeU: object, nodeV: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.edgesConnecting(N,N)"""
        pass

    @abstractmethod
    def edges(self, ):
        """public abstract java.util.Set<E> com.google.common.graph.Network.edges()"""
        pass

    @abstractmethod
    def edgeConnectingOrNull(self, endpoints: 'EndpointPair'):
        """public abstract E com.google.common.graph.Network.edgeConnectingOrNull(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, nodeU: object, nodeV: object):
        """public abstract boolean com.google.common.graph.Network.hasEdgeConnecting(N,N)"""
        pass

    @abstractmethod
    def incidentEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.incidentEdges(N)"""
        pass

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.predecessors(N)"""
        pass

    @abstractmethod
    def outDegree(self, node: object):
        """public abstract int com.google.common.graph.Network.outDegree(N)"""
        pass

    @abstractmethod
    def edgeConnectingOrNull(self, nodeU: object, nodeV: object):
        """public abstract E com.google.common.graph.Network.edgeConnectingOrNull(N,N)"""
        pass

    @abstractmethod
    def outEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.outEdges(N)"""
        pass 
 
 
# CLASS: com.google.common.graph.ElementOrder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Comparator as __Comparator
__Comparator = __Comparator
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.graph.ElementOrder as __ElementOrder_Type
__Type = __ElementOrder_Type.Type
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.graph.ElementOrder as __ElementOrder
__ElementOrder = __ElementOrder
from builtins import int
 
class ElementOrder():
    """com.google.common.graph.ElementOrder"""
 
    @staticmethod
    def __wrap(java_value: __ElementOrder) -> 'ElementOrder':
        return ElementOrder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ElementOrder):
        """
        Dynamic initializer for ElementOrder.
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
    def type(self) -> 'Type':
        """public com.google.common.graph.ElementOrder$Type com.google.common.graph.ElementOrder.type()"""
        return 'Type'.__wrap(super(ElementOrder, self).type())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.ElementOrder.toString()"""
        return str.__wrap(super(ElementOrder, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def unordered() -> 'ElementOrder':
        """public static <S> com.google.common.graph.ElementOrder<S> com.google.common.graph.ElementOrder.unordered()"""
        return ElementOrder.__wrap(__ElementOrder.unordered())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def natural() -> 'ElementOrder':
        """public static <S extends java.lang.Comparable<? super S>> com.google.common.graph.ElementOrder<S> com.google.common.graph.ElementOrder.natural()"""
        return ElementOrder.__wrap(__ElementOrder.natural())

    @staticmethod
    @overload
    def stable() -> 'ElementOrder':
        """public static <S> com.google.common.graph.ElementOrder<S> com.google.common.graph.ElementOrder.stable()"""
        return ElementOrder.__wrap(__ElementOrder.stable())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def sorted(comparator: 'Comparator') -> 'ElementOrder':
        """public static <S> com.google.common.graph.ElementOrder<S> com.google.common.graph.ElementOrder.sorted(java.util.Comparator<S>)"""
        return ElementOrder.__wrap(__ElementOrder.sorted(comparator))

    @staticmethod
    @overload
    def insertion() -> 'ElementOrder':
        """public static <S> com.google.common.graph.ElementOrder<S> com.google.common.graph.ElementOrder.insertion()"""
        return ElementOrder.__wrap(__ElementOrder.insertion())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<T> com.google.common.graph.ElementOrder.comparator()"""
        return 'Comparator'.__wrap(super(ElementOrder, self).comparator())

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.graph.ElementOrder.equals(java.lang.Object)"""
        return bool.__wrap(super(__ElementOrder, self).equals(obj))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.graph.ElementOrder.hashCode()"""
        return int.__wrap(super(ElementOrder, self).hashCode()) 
 
 
# CLASS: com.google.common.graph.AbstractValueGraph
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.google.common.graph.ValueGraph as __ValueGraph
__ValueGraph = __ValueGraph
from abc import abstractmethod, ABC
import com.google.common.graph.Graph as __Graph
__Graph = __Graph
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.google.common.graph.AbstractValueGraph as __AbstractValueGraph
__AbstractValueGraph = __AbstractValueGraph
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractValueGraph(ABC):
    """com.google.common.graph.AbstractValueGraph"""
 
    @staticmethod
    def __wrap(java_value: __AbstractValueGraph) -> 'AbstractValueGraph':
        return AbstractValueGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractValueGraph):
        """
        Dynamic initializer for AbstractValueGraph.
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

    @abstractmethod
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.ValueGraph.nodeOrder()"""
        pass

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractValueGraph.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractValueGraph, self).equals(obj))

    @overload
    def edgeValue(self, endpoints: 'EndpointPair') -> 'Optional':
        """public java.util.Optional<V> com.google.common.graph.AbstractValueGraph.edgeValue(com.google.common.graph.EndpointPair<N>)"""
        return 'Optional'.__wrap(super(__AbstractValueGraph, self).edgeValue(endpoints))

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.nodes()"""
        pass

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.successors(N)"""
        pass

    @abstractmethod
    def edgeValueOrDefault(self, endpoints: 'EndpointPair', defaultValue: object):
        """public abstract V com.google.common.graph.ValueGraph.edgeValueOrDefault(com.google.common.graph.EndpointPair<N>,V)"""
        pass

    @overload
    def __init__(self):
        """public com.google.common.graph.AbstractValueGraph()"""
        val = __AbstractValueGraph()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.predecessors(N)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractValueGraph.toString()"""
        return str.__wrap(super(AbstractValueGraph, self).toString())

    @overload
    def edgeValue(self, nodeU: object, nodeV: object) -> 'Optional':
        """public java.util.Optional<V> com.google.common.graph.AbstractValueGraph.edgeValue(N,N)"""
        return 'Optional'.__wrap(super(__AbstractValueGraph, self).edgeValue(nodeU, nodeV))

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

    @abstractmethod
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.ValueGraph.isDirected()"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def asGraph(self) -> 'Graph':
        """public com.google.common.graph.Graph<N> com.google.common.graph.AbstractValueGraph.asGraph()"""
        return 'Graph'.__wrap(super(AbstractValueGraph, self).asGraph())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def edgeValueOrDefault(self, nodeU: object, nodeV: object, defaultValue: object):
        """public abstract V com.google.common.graph.ValueGraph.edgeValueOrDefault(N,N,V)"""
        pass

    @overload
    def __init__(self, ):
        """public com.google.common.graph.AbstractValueGraph()"""
        val = __AbstractValueGraph()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractValueGraph.hashCode()"""
        return int.__wrap(super(AbstractValueGraph, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.adjacentNodes(N)"""
        pass

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.ValueGraph.allowsSelfLoops()"""
        pass 
 
 
# CLASS: com.google.common.graph.EndpointPair
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
from builtins import object
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import com.google.common.graph.EndpointPair as __EndpointPair
__EndpointPair = __EndpointPair
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.google.common.collect.UnmodifiableIterator as __UnmodifiableIterator
__UnmodifiableIterator = __UnmodifiableIterator
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class EndpointPair(ABC):
    """com.google.common.graph.EndpointPair"""
 
    @staticmethod
    def __wrap(java_value: __EndpointPair) -> 'EndpointPair':
        return EndpointPair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EndpointPair):
        """
        Dynamic initializer for EndpointPair.
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
    def nodeV(self) -> object:
        """public final N com.google.common.graph.EndpointPair.nodeV()"""
        return object.__wrap(super(EndpointPair, self).nodeV())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @abstractmethod
    def equals(self, obj: object):
        """public abstract boolean com.google.common.graph.EndpointPair.equals(java.lang.Object)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def target(self, ):
        """public abstract N com.google.common.graph.EndpointPair.target()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def iterator(self) -> 'pygcollect.UnmodifiableIterator':
        """public final com.google.common.collect.UnmodifiableIterator<N> com.google.common.graph.EndpointPair.iterator()"""
        return 'pygcollect.UnmodifiableIterator'.__wrap(super(EndpointPair, self).iterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.graph.EndpointPair.hashCode()"""
        pass

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

    @staticmethod
    @overload
    def ordered(source: object, target: object) -> 'EndpointPair':
        """public static <N> com.google.common.graph.EndpointPair<N> com.google.common.graph.EndpointPair.ordered(N,N)"""
        return EndpointPair.__wrap(__EndpointPair.ordered(source, target))

    @overload
    def nodeU(self) -> object:
        """public final N com.google.common.graph.EndpointPair.nodeU()"""
        return object.__wrap(super(EndpointPair, self).nodeU())

    @abstractmethod
    def isOrdered(self, ):
        """public abstract boolean com.google.common.graph.EndpointPair.isOrdered()"""
        pass

    @overload
    def adjacentNode(self, node: object) -> object:
        """public final N com.google.common.graph.EndpointPair.adjacentNode(N)"""
        return object.__wrap(super(__EndpointPair, self).adjacentNode(node))

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
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @staticmethod
    @overload
    def unordered(nodeU: object, nodeV: object) -> 'EndpointPair':
        """public static <N> com.google.common.graph.EndpointPair<N> com.google.common.graph.EndpointPair.unordered(N,N)"""
        return EndpointPair.__wrap(__EndpointPair.unordered(nodeU, nodeV))

    @abstractmethod
    def source(self, ):
        """public abstract N com.google.common.graph.EndpointPair.source()"""
        pass 
 
 
# CLASS: com.google.common.graph.MutableValueGraph
import com.google.common.graph.ValueGraph as __ValueGraph
__ValueGraph = __ValueGraph
import com.google.common.graph.MutableValueGraph as __MutableValueGraph
__MutableValueGraph = __MutableValueGraph
from abc import abstractmethod, ABC
 
class MutableValueGraph(ABC):
    """com.google.common.graph.MutableValueGraph"""
 
    @staticmethod
    def __wrap(java_value: __MutableValueGraph) -> 'MutableValueGraph':
        return MutableValueGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableValueGraph):
        """
        Dynamic initializer for MutableValueGraph.
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
    def edgeValue(self, nodeU: object, nodeV: object):
        """public abstract java.util.Optional<V> com.google.common.graph.ValueGraph.edgeValue(N,N)"""
        pass

    @abstractmethod
    def edgeValueOrDefault(self, endpoints: 'EndpointPair', defaultValue: object):
        """public abstract V com.google.common.graph.ValueGraph.edgeValueOrDefault(com.google.common.graph.EndpointPair<N>,V)"""
        pass

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.predecessors(N)"""
        pass

    @abstractmethod
    def removeEdge(self, nodeU: object, nodeV: object):
        """public abstract V com.google.common.graph.MutableValueGraph.removeEdge(N,N)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.graph.ValueGraph.hashCode()"""
        pass

    @abstractmethod
    def inDegree(self, node: object):
        """public abstract int com.google.common.graph.ValueGraph.inDegree(N)"""
        pass

    @abstractmethod
    def removeNode(self, node: object):
        """public abstract boolean com.google.common.graph.MutableValueGraph.removeNode(N)"""
        pass

    @abstractmethod
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.ValueGraph.isDirected()"""
        pass

    @abstractmethod
    def edgeValue(self, endpoints: 'EndpointPair'):
        """public abstract java.util.Optional<V> com.google.common.graph.ValueGraph.edgeValue(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def addNode(self, node: object):
        """public abstract boolean com.google.common.graph.MutableValueGraph.addNode(N)"""
        pass

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.ValueGraph.allowsSelfLoops()"""
        pass

    @abstractmethod
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.ValueGraph.nodeOrder()"""
        pass

    @abstractmethod
    def asGraph(self, ):
        """public abstract com.google.common.graph.Graph<N> com.google.common.graph.ValueGraph.asGraph()"""
        pass

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.nodes()"""
        pass

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.successors(N)"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, endpoints: 'EndpointPair'):
        """public abstract boolean com.google.common.graph.ValueGraph.hasEdgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def putEdgeValue(self, nodeU: object, nodeV: object, value: object):
        """public abstract V com.google.common.graph.MutableValueGraph.putEdgeValue(N,N,V)"""
        pass

    @abstractmethod
    def edges(self, ):
        """public abstract java.util.Set<com.google.common.graph.EndpointPair<N>> com.google.common.graph.ValueGraph.edges()"""
        pass

    @abstractmethod
    def removeEdge(self, endpoints: 'EndpointPair'):
        """public abstract V com.google.common.graph.MutableValueGraph.removeEdge(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def incidentEdges(self, node: object):
        """public abstract java.util.Set<com.google.common.graph.EndpointPair<N>> com.google.common.graph.ValueGraph.incidentEdges(N)"""
        pass

    @abstractmethod
    def edgeValueOrDefault(self, nodeU: object, nodeV: object, defaultValue: object):
        """public abstract V com.google.common.graph.ValueGraph.edgeValueOrDefault(N,N,V)"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, nodeU: object, nodeV: object):
        """public abstract boolean com.google.common.graph.ValueGraph.hasEdgeConnecting(N,N)"""
        pass

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.graph.ValueGraph.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def incidentEdgeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.ValueGraph.incidentEdgeOrder()"""
        pass

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.adjacentNodes(N)"""
        pass

    @abstractmethod
    def outDegree(self, node: object):
        """public abstract int com.google.common.graph.ValueGraph.outDegree(N)"""
        pass

    @abstractmethod
    def putEdgeValue(self, endpoints: 'EndpointPair', value: object):
        """public abstract V com.google.common.graph.MutableValueGraph.putEdgeValue(com.google.common.graph.EndpointPair<N>,V)"""
        pass

    @abstractmethod
    def degree(self, node: object):
        """public abstract int com.google.common.graph.ValueGraph.degree(N)"""
        pass 
 
 
# CLASS: com.google.common.graph.AbstractNetwork
import com.google.common.graph.Network as __Network
__Network = __Network
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Optional as __Optional
__Optional = __Optional
from builtins import object
from abc import abstractmethod, ABC
import com.google.common.graph.Graph as __Graph
__Graph = __Graph
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.graph.AbstractNetwork as __AbstractNetwork
__AbstractNetwork = __AbstractNetwork
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractNetwork(ABC):
    """com.google.common.graph.AbstractNetwork"""
 
    @staticmethod
    def __wrap(java_value: __AbstractNetwork) -> 'AbstractNetwork':
        return AbstractNetwork(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractNetwork):
        """
        Dynamic initializer for AbstractNetwork.
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
    def edgeConnectingOrNull(self, nodeU: object, nodeV: object) -> object:
        """public E com.google.common.graph.AbstractNetwork.edgeConnectingOrNull(N,N)"""
        return object.__wrap(super(__AbstractNetwork, self).edgeConnectingOrNull(nodeU, nodeV))

    @abstractmethod
    def incidentNodes(self, edge: object):
        """public abstract com.google.common.graph.EndpointPair<N> com.google.common.graph.Network.incidentNodes(E)"""
        pass

    @overload
    def edgeConnectingOrNull(self, endpoints: 'EndpointPair') -> object:
        """public E com.google.common.graph.AbstractNetwork.edgeConnectingOrNull(com.google.common.graph.EndpointPair<N>)"""
        return object.__wrap(super(__AbstractNetwork, self).edgeConnectingOrNull(endpoints))

    @overload
    def __init__(self, ):
        """public com.google.common.graph.AbstractNetwork()"""
        val = __AbstractNetwork()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.google.common.graph.AbstractNetwork()"""
        val = __AbstractNetwork()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def adjacentEdges(self, edge: object) -> 'Set':
        """public java.util.Set<E> com.google.common.graph.AbstractNetwork.adjacentEdges(E)"""
        return 'Set'.__wrap(super(__AbstractNetwork, self).adjacentEdges(edge))

    @overload
    def hasEdgeConnecting(self, endpoints: 'EndpointPair') -> bool:
        """public boolean com.google.common.graph.AbstractNetwork.hasEdgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        return bool.__wrap(super(__AbstractNetwork, self).hasEdgeConnecting(endpoints))

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.Network.nodes()"""
        pass

    @overload
    def degree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.degree(N)"""
        return int.__wrap(super(__AbstractNetwork, self).degree(node))

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.adjacentNodes(N)"""
        pass

    @overload
    def inDegree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.inDegree(N)"""
        return int.__wrap(super(__AbstractNetwork, self).inDegree(node))

    @overload
    def outDegree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.outDegree(N)"""
        return int.__wrap(super(__AbstractNetwork, self).outDegree(node))

    @abstractmethod
    def inEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.inEdges(N)"""
        pass

    @override
    @overload
    def asGraph(self) -> 'Graph':
        """public com.google.common.graph.Graph<N> com.google.common.graph.AbstractNetwork.asGraph()"""
        return 'Graph'.__wrap(super(AbstractNetwork, self).asGraph())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def allowsParallelEdges(self, ):
        """public abstract boolean com.google.common.graph.Network.allowsParallelEdges()"""
        pass

    @overload
    def edgeConnecting(self, endpoints: 'EndpointPair') -> 'Optional':
        """public java.util.Optional<E> com.google.common.graph.AbstractNetwork.edgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        return 'Optional'.__wrap(super(__AbstractNetwork, self).edgeConnecting(endpoints))

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.Network.allowsSelfLoops()"""
        pass

    @abstractmethod
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.Network.isDirected()"""
        pass

    @abstractmethod
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.Network.nodeOrder()"""
        pass

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractNetwork.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractNetwork, self).equals(obj))

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.successors(N)"""
        pass

    @abstractmethod
    def edgeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<E> com.google.common.graph.Network.edgeOrder()"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractNetwork.hashCode()"""
        return int.__wrap(super(AbstractNetwork, self).hashCode())

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

    @overload
    def hasEdgeConnecting(self, nodeU: object, nodeV: object) -> bool:
        """public boolean com.google.common.graph.AbstractNetwork.hasEdgeConnecting(N,N)"""
        return bool.__wrap(super(__AbstractNetwork, self).hasEdgeConnecting(nodeU, nodeV))

    @abstractmethod
    def edges(self, ):
        """public abstract java.util.Set<E> com.google.common.graph.Network.edges()"""
        pass

    @overload
    def edgesConnecting(self, endpoints: 'EndpointPair') -> 'Set':
        """public java.util.Set<E> com.google.common.graph.AbstractNetwork.edgesConnecting(com.google.common.graph.EndpointPair<N>)"""
        return 'Set'.__wrap(super(__AbstractNetwork, self).edgesConnecting(endpoints))

    @overload
    def edgeConnecting(self, nodeU: object, nodeV: object) -> 'Optional':
        """public java.util.Optional<E> com.google.common.graph.AbstractNetwork.edgeConnecting(N,N)"""
        return 'Optional'.__wrap(super(__AbstractNetwork, self).edgeConnecting(nodeU, nodeV))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def incidentEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.incidentEdges(N)"""
        pass

    @overload
    def edgesConnecting(self, nodeU: object, nodeV: object) -> 'Set':
        """public java.util.Set<E> com.google.common.graph.AbstractNetwork.edgesConnecting(N,N)"""
        return 'Set'.__wrap(super(__AbstractNetwork, self).edgesConnecting(nodeU, nodeV))

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.predecessors(N)"""
        pass

    @abstractmethod
    def outEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.outEdges(N)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractNetwork.toString()"""
        return str.__wrap(super(AbstractNetwork, self).toString()) 
 
 
# CLASS: com.google.common.graph.AbstractGraph
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import com.google.common.graph.Graph as __Graph
__Graph = __Graph
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.graph.AbstractGraph as __AbstractGraph
__AbstractGraph = __AbstractGraph
from builtins import int
 
class AbstractGraph(ABC):
    """com.google.common.graph.AbstractGraph"""
 
    @staticmethod
    def __wrap(java_value: __AbstractGraph) -> 'AbstractGraph':
        return AbstractGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractGraph):
        """
        Dynamic initializer for AbstractGraph.
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

    @abstractmethod
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.Graph.isDirected()"""
        pass

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.predecessors(N)"""
        pass

    @overload
    def __init__(self, ):
        """public com.google.common.graph.AbstractGraph()"""
        val = __AbstractGraph()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.nodes()"""
        pass

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.adjacentNodes(N)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.Graph.nodeOrder()"""
        pass

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

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.successors(N)"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.Graph.allowsSelfLoops()"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractGraph.hashCode()"""
        return int.__wrap(super(AbstractGraph, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractGraph.toString()"""
        return str.__wrap(super(AbstractGraph, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.google.common.graph.AbstractGraph()"""
        val = __AbstractGraph()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractGraph.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractGraph, self).equals(obj)) 
 
 
# CLASS: com.google.common.graph.MutableNetwork
import com.google.common.graph.Network as __Network
__Network = __Network
import com.google.common.graph.MutableNetwork as __MutableNetwork
__MutableNetwork = __MutableNetwork
from abc import abstractmethod, ABC
 
class MutableNetwork(ABC):
    """com.google.common.graph.MutableNetwork"""
 
    @staticmethod
    def __wrap(java_value: __MutableNetwork) -> 'MutableNetwork':
        return MutableNetwork(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableNetwork):
        """
        Dynamic initializer for MutableNetwork.
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
    def incidentNodes(self, edge: object):
        """public abstract com.google.common.graph.EndpointPair<N> com.google.common.graph.Network.incidentNodes(E)"""
        pass

    @abstractmethod
    def adjacentEdges(self, edge: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.adjacentEdges(E)"""
        pass

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.Network.nodes()"""
        pass

    @abstractmethod
    def degree(self, node: object):
        """public abstract int com.google.common.graph.Network.degree(N)"""
        pass

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.adjacentNodes(N)"""
        pass

    @abstractmethod
    def inEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.inEdges(N)"""
        pass

    @abstractmethod
    def allowsParallelEdges(self, ):
        """public abstract boolean com.google.common.graph.Network.allowsParallelEdges()"""
        pass

    @abstractmethod
    def addEdge(self, endpoints: 'EndpointPair', edge: object):
        """public abstract boolean com.google.common.graph.MutableNetwork.addEdge(com.google.common.graph.EndpointPair<N>,E)"""
        pass

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.graph.Network.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def addNode(self, node: object):
        """public abstract boolean com.google.common.graph.MutableNetwork.addNode(N)"""
        pass

    @abstractmethod
    def removeNode(self, node: object):
        """public abstract boolean com.google.common.graph.MutableNetwork.removeNode(N)"""
        pass

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.Network.allowsSelfLoops()"""
        pass

    @abstractmethod
    def addEdge(self, nodeU: object, nodeV: object, edge: object):
        """public abstract boolean com.google.common.graph.MutableNetwork.addEdge(N,N,E)"""
        pass

    @abstractmethod
    def edgeConnecting(self, endpoints: 'EndpointPair'):
        """public abstract java.util.Optional<E> com.google.common.graph.Network.edgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.graph.Network.hashCode()"""
        pass

    @abstractmethod
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.Network.isDirected()"""
        pass

    @abstractmethod
    def asGraph(self, ):
        """public abstract com.google.common.graph.Graph<N> com.google.common.graph.Network.asGraph()"""
        pass

    @abstractmethod
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.Network.nodeOrder()"""
        pass

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.successors(N)"""
        pass

    @abstractmethod
    def inDegree(self, node: object):
        """public abstract int com.google.common.graph.Network.inDegree(N)"""
        pass

    @abstractmethod
    def removeEdge(self, edge: object):
        """public abstract boolean com.google.common.graph.MutableNetwork.removeEdge(E)"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, endpoints: 'EndpointPair'):
        """public abstract boolean com.google.common.graph.Network.hasEdgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def edgeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<E> com.google.common.graph.Network.edgeOrder()"""
        pass

    @abstractmethod
    def edgeConnecting(self, nodeU: object, nodeV: object):
        """public abstract java.util.Optional<E> com.google.common.graph.Network.edgeConnecting(N,N)"""
        pass

    @abstractmethod
    def edgesConnecting(self, endpoints: 'EndpointPair'):
        """public abstract java.util.Set<E> com.google.common.graph.Network.edgesConnecting(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def edgesConnecting(self, nodeU: object, nodeV: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.edgesConnecting(N,N)"""
        pass

    @abstractmethod
    def edges(self, ):
        """public abstract java.util.Set<E> com.google.common.graph.Network.edges()"""
        pass

    @abstractmethod
    def edgeConnectingOrNull(self, endpoints: 'EndpointPair'):
        """public abstract E com.google.common.graph.Network.edgeConnectingOrNull(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, nodeU: object, nodeV: object):
        """public abstract boolean com.google.common.graph.Network.hasEdgeConnecting(N,N)"""
        pass

    @abstractmethod
    def incidentEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.incidentEdges(N)"""
        pass

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.predecessors(N)"""
        pass

    @abstractmethod
    def outDegree(self, node: object):
        """public abstract int com.google.common.graph.Network.outDegree(N)"""
        pass

    @abstractmethod
    def edgeConnectingOrNull(self, nodeU: object, nodeV: object):
        """public abstract E com.google.common.graph.Network.edgeConnectingOrNull(N,N)"""
        pass

    @abstractmethod
    def outEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.outEdges(N)"""
        pass 
 
 
# CLASS: com.google.common.graph.GraphBuilder
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.graph.ImmutableGraph as __ImmutableGraph_Builder
__Builder = __ImmutableGraph_Builder.Builder
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.graph.MutableGraph as __MutableGraph
__MutableGraph = __MutableGraph
import com.google.common.graph.GraphBuilder as __GraphBuilder
__GraphBuilder = __GraphBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GraphBuilder():
    """com.google.common.graph.GraphBuilder"""
 
    @staticmethod
    def __wrap(java_value: __GraphBuilder) -> 'GraphBuilder':
        return GraphBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GraphBuilder):
        """
        Dynamic initializer for GraphBuilder.
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
 
    @staticmethod
    @overload
    def directed() -> 'GraphBuilder':
        """public static com.google.common.graph.GraphBuilder<java.lang.Object> com.google.common.graph.GraphBuilder.directed()"""
        return GraphBuilder.__wrap(__GraphBuilder.directed())

    @staticmethod
    @overload
    def undirected() -> 'GraphBuilder':
        """public static com.google.common.graph.GraphBuilder<java.lang.Object> com.google.common.graph.GraphBuilder.undirected()"""
        return GraphBuilder.__wrap(__GraphBuilder.undirected())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def build(self) -> 'MutableGraph':
        """public <N1 extends N> com.google.common.graph.MutableGraph<N1> com.google.common.graph.GraphBuilder.build()"""
        return 'MutableGraph'.__wrap(super(GraphBuilder, self).build())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def expectedNodeCount(self, expectedNodeCount: int) -> 'GraphBuilder':
        """public com.google.common.graph.GraphBuilder<N> com.google.common.graph.GraphBuilder.expectedNodeCount(int)"""
        return 'GraphBuilder'.__wrap(super(__GraphBuilder, self).expectedNodeCount(__int.valueOf(expectedNodeCount)))

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

    @staticmethod
    @overload
    def from(graph: 'Graph') -> 'GraphBuilder':
        """public static <N> com.google.common.graph.GraphBuilder<N> com.google.common.graph.GraphBuilder.from(com.google.common.graph.Graph<N>)"""
        return GraphBuilder.__wrap(__GraphBuilder.from(graph))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def incidentEdgeOrder(self, incidentEdgeOrder: 'ElementOrder') -> 'GraphBuilder':
        """public <N1 extends N> com.google.common.graph.GraphBuilder<N1> com.google.common.graph.GraphBuilder.incidentEdgeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'GraphBuilder'.__wrap(super(__GraphBuilder, self).incidentEdgeOrder(incidentEdgeOrder))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def nodeOrder(self, nodeOrder: 'ElementOrder') -> 'GraphBuilder':
        """public <N1 extends N> com.google.common.graph.GraphBuilder<N1> com.google.common.graph.GraphBuilder.nodeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'GraphBuilder'.__wrap(super(__GraphBuilder, self).nodeOrder(nodeOrder))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def allowsSelfLoops(self, allowsSelfLoops: bool) -> 'GraphBuilder':
        """public com.google.common.graph.GraphBuilder<N> com.google.common.graph.GraphBuilder.allowsSelfLoops(boolean)"""
        return 'GraphBuilder'.__wrap(super(__GraphBuilder, self).allowsSelfLoops(__boolean.valueOf(allowsSelfLoops)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def immutable(self) -> 'Builder':
        """public <N1 extends N> com.google.common.graph.ImmutableGraph$Builder<N1> com.google.common.graph.GraphBuilder.immutable()"""
        return 'Builder'.__wrap(super(GraphBuilder, self).immutable())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.graph.ImmutableNetwork
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.graph.ImmutableGraph as __ImmutableGraph
__ImmutableGraph = __ImmutableGraph
from builtins import type
import java.util.Set as __Set
__Set = __Set
import java.util.Optional as __Optional
__Optional = __Optional
from builtins import object
import com.google.common.graph.ImmutableNetwork as __ImmutableNetwork
__ImmutableNetwork = __ImmutableNetwork
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.graph.AbstractNetwork as __AbstractNetwork
__AbstractNetwork = __AbstractNetwork
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ImmutableNetwork():
    """com.google.common.graph.ImmutableNetwork"""
 
    @staticmethod
    def __wrap(java_value: __ImmutableNetwork) -> 'ImmutableNetwork':
        return ImmutableNetwork(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutableNetwork):
        """
        Dynamic initializer for ImmutableNetwork.
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

    @staticmethod
    @overload
    def copyOf(network: 'ImmutableNetwork') -> 'ImmutableNetwork':
        """public static <N,E> com.google.common.graph.ImmutableNetwork<N, E> com.google.common.graph.ImmutableNetwork.copyOf(com.google.common.graph.ImmutableNetwork<N, E>)"""
        return ImmutableNetwork.__wrap(__ImmutableNetwork.copyOf(network))

    @override
    @overload
    def asGraph(self) -> 'ImmutableGraph':
        """public com.google.common.graph.ImmutableGraph<N> com.google.common.graph.ImmutableNetwork.asGraph()"""
        return 'ImmutableGraph'.__wrap(super(ImmutableNetwork, self).asGraph())

    @overload
    def edgeConnectingOrNull(self, nodeU: object, nodeV: object) -> object:
        """public E com.google.common.graph.AbstractNetwork.edgeConnectingOrNull(N,N)"""
        return object.__wrap(super(__AbstractNetwork, self).edgeConnectingOrNull(nodeU, nodeV))

    @staticmethod
    @overload
    def copyOf(network: 'Network') -> 'ImmutableNetwork':
        """public static <N,E> com.google.common.graph.ImmutableNetwork<N, E> com.google.common.graph.ImmutableNetwork.copyOf(com.google.common.graph.Network<N, E>)"""
        return ImmutableNetwork.__wrap(__ImmutableNetwork.copyOf(network))

    @overload
    def edgeConnectingOrNull(self, endpoints: 'EndpointPair') -> object:
        """public E com.google.common.graph.AbstractNetwork.edgeConnectingOrNull(com.google.common.graph.EndpointPair<N>)"""
        return object.__wrap(super(__AbstractNetwork, self).edgeConnectingOrNull(endpoints))

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractNetwork.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractNetwork, self).equals(obj))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def adjacentEdges(self, edge: object) -> 'Set':
        """public java.util.Set<E> com.google.common.graph.AbstractNetwork.adjacentEdges(E)"""
        return 'Set'.__wrap(super(__AbstractNetwork, self).adjacentEdges(edge))

    @overload
    def hasEdgeConnecting(self, endpoints: 'EndpointPair') -> bool:
        """public boolean com.google.common.graph.AbstractNetwork.hasEdgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        return bool.__wrap(super(__AbstractNetwork, self).hasEdgeConnecting(endpoints))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractNetwork.hashCode()"""
        return int.__wrap(super(AbstractNetwork, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def degree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.degree(N)"""
        return int.__wrap(super(__AbstractNetwork, self).degree(node))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def inDegree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.inDegree(N)"""
        return int.__wrap(super(__AbstractNetwork, self).inDegree(node))

    @overload
    def outDegree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.outDegree(N)"""
        return int.__wrap(super(__AbstractNetwork, self).outDegree(node))

    @overload
    def hasEdgeConnecting(self, nodeU: object, nodeV: object) -> bool:
        """public boolean com.google.common.graph.AbstractNetwork.hasEdgeConnecting(N,N)"""
        return bool.__wrap(super(__AbstractNetwork, self).hasEdgeConnecting(nodeU, nodeV))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def edgesConnecting(self, endpoints: 'EndpointPair') -> 'Set':
        """public java.util.Set<E> com.google.common.graph.AbstractNetwork.edgesConnecting(com.google.common.graph.EndpointPair<N>)"""
        return 'Set'.__wrap(super(__AbstractNetwork, self).edgesConnecting(endpoints))

    @overload
    def edgeConnecting(self, nodeU: object, nodeV: object) -> 'Optional':
        """public java.util.Optional<E> com.google.common.graph.AbstractNetwork.edgeConnecting(N,N)"""
        return 'Optional'.__wrap(super(__AbstractNetwork, self).edgeConnecting(nodeU, nodeV))

    @overload
    def edgeConnecting(self, endpoints: 'EndpointPair') -> 'Optional':
        """public java.util.Optional<E> com.google.common.graph.AbstractNetwork.edgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        return 'Optional'.__wrap(super(__AbstractNetwork, self).edgeConnecting(endpoints))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractNetwork.toString()"""
        return str.__wrap(super(AbstractNetwork, self).toString()) 
 
 
# CLASS: com.google.common.graph.ElementOrder$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.graph.ElementOrder as __ElementOrder_Type
__Type = __ElementOrder_Type.Type
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Type():
    """com.google.common.graph.ElementOrder.Type"""
 
    @staticmethod
    def __wrap(java_value: __Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Type):
        """
        Dynamic initializer for Type.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.google.common.graph.ElementOrder$Type[] com.google.common.graph.ElementOrder$Type.values()"""
        return List[Type].__wrap(__Type.values())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(name: str) -> 'Type':
        """public static com.google.common.graph.ElementOrder$Type com.google.common.graph.ElementOrder$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(name))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.google.common.graph.Graph
import com.google.common.graph.Graph as __Graph
__Graph = __Graph
from abc import abstractmethod, ABC
 
class Graph(ABC):
    """com.google.common.graph.Graph"""
 
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
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.Graph.isDirected()"""
        pass

    @abstractmethod
    def degree(self, node: object):
        """public abstract int com.google.common.graph.Graph.degree(N)"""
        pass

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.predecessors(N)"""
        pass

    @abstractmethod
    def inDegree(self, node: object):
        """public abstract int com.google.common.graph.Graph.inDegree(N)"""
        pass

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.nodes()"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, endpoints: 'EndpointPair'):
        """public abstract boolean com.google.common.graph.Graph.hasEdgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.adjacentNodes(N)"""
        pass

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.graph.Graph.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def outDegree(self, node: object):
        """public abstract int com.google.common.graph.Graph.outDegree(N)"""
        pass

    @abstractmethod
    def incidentEdgeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.Graph.incidentEdgeOrder()"""
        pass

    @abstractmethod
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.Graph.nodeOrder()"""
        pass

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.successors(N)"""
        pass

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.Graph.allowsSelfLoops()"""
        pass

    @abstractmethod
    def edges(self, ):
        """public abstract java.util.Set<com.google.common.graph.EndpointPair<N>> com.google.common.graph.Graph.edges()"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, nodeU: object, nodeV: object):
        """public abstract boolean com.google.common.graph.Graph.hasEdgeConnecting(N,N)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.graph.Graph.hashCode()"""
        pass

    @abstractmethod
    def incidentEdges(self, node: object):
        """public abstract java.util.Set<com.google.common.graph.EndpointPair<N>> com.google.common.graph.Graph.incidentEdges(N)"""
        pass 
 
 
# CLASS: com.google.common.graph.ImmutableValueGraph$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.graph.ImmutableValueGraph as __ImmutableValueGraph_Builder
__Builder = __ImmutableValueGraph_Builder.Builder
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.graph.ImmutableValueGraph as __ImmutableValueGraph
__ImmutableValueGraph = __ImmutableValueGraph
from builtins import int
 
class Builder():
    """com.google.common.graph.ImmutableValueGraph.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def build(self) -> 'ImmutableValueGraph':
        """public com.google.common.graph.ImmutableValueGraph<N, V> com.google.common.graph.ImmutableValueGraph$Builder.build()"""
        return 'ImmutableValueGraph'.__wrap(super(Builder, self).build())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def putEdgeValue(self, endpoints: 'EndpointPair', value: object) -> 'Builder':
        """public com.google.common.graph.ImmutableValueGraph$Builder<N, V> com.google.common.graph.ImmutableValueGraph$Builder.putEdgeValue(com.google.common.graph.EndpointPair<N>,V)"""
        return 'Builder'.__wrap(super(__Builder, self).putEdgeValue(endpoints, value))

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

    @overload
    def putEdgeValue(self, nodeU: object, nodeV: object, value: object) -> 'Builder':
        """public com.google.common.graph.ImmutableValueGraph$Builder<N, V> com.google.common.graph.ImmutableValueGraph$Builder.putEdgeValue(N,N,V)"""
        return 'Builder'.__wrap(super(__Builder, self).putEdgeValue(nodeU, nodeV, value))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addNode(self, node: object) -> 'Builder':
        """public com.google.common.graph.ImmutableValueGraph$Builder<N, V> com.google.common.graph.ImmutableValueGraph$Builder.addNode(N)"""
        return 'Builder'.__wrap(super(__Builder, self).addNode(node))

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
 
 
# CLASS: com.google.common.graph.MutableGraph
import com.google.common.graph.Graph as __Graph
__Graph = __Graph
import com.google.common.graph.MutableGraph as __MutableGraph
__MutableGraph = __MutableGraph
from abc import abstractmethod, ABC
 
class MutableGraph(ABC):
    """com.google.common.graph.MutableGraph"""
 
    @staticmethod
    def __wrap(java_value: __MutableGraph) -> 'MutableGraph':
        return MutableGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableGraph):
        """
        Dynamic initializer for MutableGraph.
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
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.Graph.isDirected()"""
        pass

    @abstractmethod
    def degree(self, node: object):
        """public abstract int com.google.common.graph.Graph.degree(N)"""
        pass

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.predecessors(N)"""
        pass

    @abstractmethod
    def inDegree(self, node: object):
        """public abstract int com.google.common.graph.Graph.inDegree(N)"""
        pass

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.nodes()"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, endpoints: 'EndpointPair'):
        """public abstract boolean com.google.common.graph.Graph.hasEdgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.adjacentNodes(N)"""
        pass

    @abstractmethod
    def removeEdge(self, nodeU: object, nodeV: object):
        """public abstract boolean com.google.common.graph.MutableGraph.removeEdge(N,N)"""
        pass

    @abstractmethod
    def addNode(self, node: object):
        """public abstract boolean com.google.common.graph.MutableGraph.addNode(N)"""
        pass

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.graph.Graph.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def outDegree(self, node: object):
        """public abstract int com.google.common.graph.Graph.outDegree(N)"""
        pass

    @abstractmethod
    def incidentEdgeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.Graph.incidentEdgeOrder()"""
        pass

    @abstractmethod
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.Graph.nodeOrder()"""
        pass

    @abstractmethod
    def removeNode(self, node: object):
        """public abstract boolean com.google.common.graph.MutableGraph.removeNode(N)"""
        pass

    @abstractmethod
    def removeEdge(self, endpoints: 'EndpointPair'):
        """public abstract boolean com.google.common.graph.MutableGraph.removeEdge(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.successors(N)"""
        pass

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.Graph.allowsSelfLoops()"""
        pass

    @abstractmethod
    def putEdge(self, nodeU: object, nodeV: object):
        """public abstract boolean com.google.common.graph.MutableGraph.putEdge(N,N)"""
        pass

    @abstractmethod
    def edges(self, ):
        """public abstract java.util.Set<com.google.common.graph.EndpointPair<N>> com.google.common.graph.Graph.edges()"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, nodeU: object, nodeV: object):
        """public abstract boolean com.google.common.graph.Graph.hasEdgeConnecting(N,N)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.graph.Graph.hashCode()"""
        pass

    @abstractmethod
    def incidentEdges(self, node: object):
        """public abstract java.util.Set<com.google.common.graph.EndpointPair<N>> com.google.common.graph.Graph.incidentEdges(N)"""
        pass

    @abstractmethod
    def putEdge(self, endpoints: 'EndpointPair'):
        """public abstract boolean com.google.common.graph.MutableGraph.putEdge(com.google.common.graph.EndpointPair<N>)"""
        pass 
 
 
# CLASS: com.google.common.graph.NetworkBuilder
import com.google.common.graph.MutableNetwork as __MutableNetwork
__MutableNetwork = __MutableNetwork
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.graph.ImmutableNetwork as __ImmutableNetwork_Builder
__Builder = __ImmutableNetwork_Builder.Builder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.google.common.graph.NetworkBuilder as __NetworkBuilder
__NetworkBuilder = __NetworkBuilder
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NetworkBuilder():
    """com.google.common.graph.NetworkBuilder"""
 
    @staticmethod
    def __wrap(java_value: __NetworkBuilder) -> 'NetworkBuilder':
        return NetworkBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NetworkBuilder):
        """
        Dynamic initializer for NetworkBuilder.
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

    @staticmethod
    @overload
    def from(network: 'Network') -> 'NetworkBuilder':
        """public static <N,E> com.google.common.graph.NetworkBuilder<N, E> com.google.common.graph.NetworkBuilder.from(com.google.common.graph.Network<N, E>)"""
        return NetworkBuilder.__wrap(__NetworkBuilder.from(network))

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
    def edgeOrder(self, edgeOrder: 'ElementOrder') -> 'NetworkBuilder':
        """public <E1 extends E> com.google.common.graph.NetworkBuilder<N, E1> com.google.common.graph.NetworkBuilder.edgeOrder(com.google.common.graph.ElementOrder<E1>)"""
        return 'NetworkBuilder'.__wrap(super(__NetworkBuilder, self).edgeOrder(edgeOrder))

    @overload
    def expectedEdgeCount(self, expectedEdgeCount: int) -> 'NetworkBuilder':
        """public com.google.common.graph.NetworkBuilder<N, E> com.google.common.graph.NetworkBuilder.expectedEdgeCount(int)"""
        return 'NetworkBuilder'.__wrap(super(__NetworkBuilder, self).expectedEdgeCount(__int.valueOf(expectedEdgeCount)))

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

    @overload
    def expectedNodeCount(self, expectedNodeCount: int) -> 'NetworkBuilder':
        """public com.google.common.graph.NetworkBuilder<N, E> com.google.common.graph.NetworkBuilder.expectedNodeCount(int)"""
        return 'NetworkBuilder'.__wrap(super(__NetworkBuilder, self).expectedNodeCount(__int.valueOf(expectedNodeCount)))

    @overload
    def build(self) -> 'MutableNetwork':
        """public <N1 extends N,E1 extends E> com.google.common.graph.MutableNetwork<N1, E1> com.google.common.graph.NetworkBuilder.build()"""
        return 'MutableNetwork'.__wrap(super(NetworkBuilder, self).build())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def allowsSelfLoops(self, allowsSelfLoops: bool) -> 'NetworkBuilder':
        """public com.google.common.graph.NetworkBuilder<N, E> com.google.common.graph.NetworkBuilder.allowsSelfLoops(boolean)"""
        return 'NetworkBuilder'.__wrap(super(__NetworkBuilder, self).allowsSelfLoops(__boolean.valueOf(allowsSelfLoops)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def directed() -> 'NetworkBuilder':
        """public static com.google.common.graph.NetworkBuilder<java.lang.Object, java.lang.Object> com.google.common.graph.NetworkBuilder.directed()"""
        return NetworkBuilder.__wrap(__NetworkBuilder.directed())

    @overload
    def immutable(self) -> 'Builder':
        """public <N1 extends N,E1 extends E> com.google.common.graph.ImmutableNetwork$Builder<N1, E1> com.google.common.graph.NetworkBuilder.immutable()"""
        return 'Builder'.__wrap(super(NetworkBuilder, self).immutable())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def nodeOrder(self, nodeOrder: 'ElementOrder') -> 'NetworkBuilder':
        """public <N1 extends N> com.google.common.graph.NetworkBuilder<N1, E> com.google.common.graph.NetworkBuilder.nodeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'NetworkBuilder'.__wrap(super(__NetworkBuilder, self).nodeOrder(nodeOrder))

    @staticmethod
    @overload
    def undirected() -> 'NetworkBuilder':
        """public static com.google.common.graph.NetworkBuilder<java.lang.Object, java.lang.Object> com.google.common.graph.NetworkBuilder.undirected()"""
        return NetworkBuilder.__wrap(__NetworkBuilder.undirected())

    @overload
    def allowsParallelEdges(self, allowsParallelEdges: bool) -> 'NetworkBuilder':
        """public com.google.common.graph.NetworkBuilder<N, E> com.google.common.graph.NetworkBuilder.allowsParallelEdges(boolean)"""
        return 'NetworkBuilder'.__wrap(super(__NetworkBuilder, self).allowsParallelEdges(__boolean.valueOf(allowsParallelEdges)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.graph.ValueGraph
import com.google.common.graph.ValueGraph as __ValueGraph
__ValueGraph = __ValueGraph
from abc import abstractmethod, ABC
 
class ValueGraph(ABC):
    """com.google.common.graph.ValueGraph"""
 
    @staticmethod
    def __wrap(java_value: __ValueGraph) -> 'ValueGraph':
        return ValueGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueGraph):
        """
        Dynamic initializer for ValueGraph.
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
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.ValueGraph.nodeOrder()"""
        pass

    @abstractmethod
    def asGraph(self, ):
        """public abstract com.google.common.graph.Graph<N> com.google.common.graph.ValueGraph.asGraph()"""
        pass

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.nodes()"""
        pass

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.successors(N)"""
        pass

    @abstractmethod
    def edgeValue(self, nodeU: object, nodeV: object):
        """public abstract java.util.Optional<V> com.google.common.graph.ValueGraph.edgeValue(N,N)"""
        pass

    @abstractmethod
    def edgeValueOrDefault(self, endpoints: 'EndpointPair', defaultValue: object):
        """public abstract V com.google.common.graph.ValueGraph.edgeValueOrDefault(com.google.common.graph.EndpointPair<N>,V)"""
        pass

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.predecessors(N)"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.graph.ValueGraph.hashCode()"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, endpoints: 'EndpointPair'):
        """public abstract boolean com.google.common.graph.ValueGraph.hasEdgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def inDegree(self, node: object):
        """public abstract int com.google.common.graph.ValueGraph.inDegree(N)"""
        pass

    @abstractmethod
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.ValueGraph.isDirected()"""
        pass

    @abstractmethod
    def edges(self, ):
        """public abstract java.util.Set<com.google.common.graph.EndpointPair<N>> com.google.common.graph.ValueGraph.edges()"""
        pass

    @abstractmethod
    def incidentEdges(self, node: object):
        """public abstract java.util.Set<com.google.common.graph.EndpointPair<N>> com.google.common.graph.ValueGraph.incidentEdges(N)"""
        pass

    @abstractmethod
    def edgeValue(self, endpoints: 'EndpointPair'):
        """public abstract java.util.Optional<V> com.google.common.graph.ValueGraph.edgeValue(com.google.common.graph.EndpointPair<N>)"""
        pass

    @abstractmethod
    def edgeValueOrDefault(self, nodeU: object, nodeV: object, defaultValue: object):
        """public abstract V com.google.common.graph.ValueGraph.edgeValueOrDefault(N,N,V)"""
        pass

    @abstractmethod
    def hasEdgeConnecting(self, nodeU: object, nodeV: object):
        """public abstract boolean com.google.common.graph.ValueGraph.hasEdgeConnecting(N,N)"""
        pass

    @abstractmethod
    def equals(self, object: object):
        """public abstract boolean com.google.common.graph.ValueGraph.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def incidentEdgeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.ValueGraph.incidentEdgeOrder()"""
        pass

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.adjacentNodes(N)"""
        pass

    @abstractmethod
    def outDegree(self, node: object):
        """public abstract int com.google.common.graph.ValueGraph.outDegree(N)"""
        pass

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.ValueGraph.allowsSelfLoops()"""
        pass

    @abstractmethod
    def degree(self, node: object):
        """public abstract int com.google.common.graph.ValueGraph.degree(N)"""
        pass 
 
 
# CLASS: com.google.common.graph.ImmutableValueGraph
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.graph.ImmutableGraph as __ImmutableGraph
__ImmutableGraph = __ImmutableGraph
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.google.common.graph.AbstractValueGraph as __AbstractValueGraph
__AbstractValueGraph = __AbstractValueGraph
import java.lang.Integer as __int
from builtins import bool
import com.google.common.graph.ImmutableValueGraph as __ImmutableValueGraph
__ImmutableValueGraph = __ImmutableValueGraph
import com.google.common.graph.ElementOrder as __ElementOrder
__ElementOrder = __ElementOrder
from builtins import int
 
class ImmutableValueGraph():
    """com.google.common.graph.ImmutableValueGraph"""
 
    @staticmethod
    def __wrap(java_value: __ImmutableValueGraph) -> 'ImmutableValueGraph':
        return ImmutableValueGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImmutableValueGraph):
        """
        Dynamic initializer for ImmutableValueGraph.
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

    @staticmethod
    @overload
    def copyOf(graph: 'ValueGraph') -> 'ImmutableValueGraph':
        """public static <N,V> com.google.common.graph.ImmutableValueGraph<N, V> com.google.common.graph.ImmutableValueGraph.copyOf(com.google.common.graph.ValueGraph<N, V>)"""
        return ImmutableValueGraph.__wrap(__ImmutableValueGraph.copyOf(graph))

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractValueGraph.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractValueGraph, self).equals(obj))

    @overload
    def edgeValue(self, endpoints: 'EndpointPair') -> 'Optional':
        """public java.util.Optional<V> com.google.common.graph.AbstractValueGraph.edgeValue(com.google.common.graph.EndpointPair<N>)"""
        return 'Optional'.__wrap(super(__AbstractValueGraph, self).edgeValue(endpoints))

    @override
    @overload
    def incidentEdgeOrder(self) -> 'ElementOrder':
        """public com.google.common.graph.ElementOrder<N> com.google.common.graph.ImmutableValueGraph.incidentEdgeOrder()"""
        return 'ElementOrder'.__wrap(super(ImmutableValueGraph, self).incidentEdgeOrder())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractValueGraph.toString()"""
        return str.__wrap(super(AbstractValueGraph, self).toString())

    @overload
    def edgeValue(self, nodeU: object, nodeV: object) -> 'Optional':
        """public java.util.Optional<V> com.google.common.graph.AbstractValueGraph.edgeValue(N,N)"""
        return 'Optional'.__wrap(super(__AbstractValueGraph, self).edgeValue(nodeU, nodeV))

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
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractValueGraph.hashCode()"""
        return int.__wrap(super(AbstractValueGraph, self).hashCode())

    @staticmethod
    @overload
    def copyOf(graph: 'ImmutableValueGraph') -> 'ImmutableValueGraph':
        """public static <N,V> com.google.common.graph.ImmutableValueGraph<N, V> com.google.common.graph.ImmutableValueGraph.copyOf(com.google.common.graph.ImmutableValueGraph<N, V>)"""
        return ImmutableValueGraph.__wrap(__ImmutableValueGraph.copyOf(graph))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def asGraph(self) -> 'ImmutableGraph':
        """public com.google.common.graph.ImmutableGraph<N> com.google.common.graph.ImmutableValueGraph.asGraph()"""
        return 'ImmutableGraph'.__wrap(super(ImmutableValueGraph, self).asGraph()) 
 
 
# CLASS: com.google.common.graph.SuccessorsFunction
import com.google.common.graph.SuccessorsFunction as __SuccessorsFunction
__SuccessorsFunction = __SuccessorsFunction
from abc import abstractmethod, ABC
 
class SuccessorsFunction(ABC):
    """com.google.common.graph.SuccessorsFunction"""
 
    @staticmethod
    def __wrap(java_value: __SuccessorsFunction) -> 'SuccessorsFunction':
        return SuccessorsFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SuccessorsFunction):
        """
        Dynamic initializer for SuccessorsFunction.
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
    def successors(self, node: object):
        """public abstract java.lang.Iterable<? extends N> com.google.common.graph.SuccessorsFunction.successors(N)"""
        pass 
 
 
# CLASS: com.google.common.graph.ImmutableNetwork$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.graph.ImmutableNetwork as __ImmutableNetwork_Builder
__Builder = __ImmutableNetwork_Builder.Builder
import com.google.common.graph.ImmutableNetwork as __ImmutableNetwork
__ImmutableNetwork = __ImmutableNetwork
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
 
class Builder():
    """com.google.common.graph.ImmutableNetwork.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def addEdge(self, nodeU: object, nodeV: object, edge: object) -> 'Builder':
        """public com.google.common.graph.ImmutableNetwork$Builder<N, E> com.google.common.graph.ImmutableNetwork$Builder.addEdge(N,N,E)"""
        return 'Builder'.__wrap(super(__Builder, self).addEdge(nodeU, nodeV, edge))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def build(self) -> 'ImmutableNetwork':
        """public com.google.common.graph.ImmutableNetwork<N, E> com.google.common.graph.ImmutableNetwork$Builder.build()"""
        return 'ImmutableNetwork'.__wrap(super(Builder, self).build())

    @overload
    def addNode(self, node: object) -> 'Builder':
        """public com.google.common.graph.ImmutableNetwork$Builder<N, E> com.google.common.graph.ImmutableNetwork$Builder.addNode(N)"""
        return 'Builder'.__wrap(super(__Builder, self).addNode(node))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addEdge(self, endpoints: 'EndpointPair', edge: object) -> 'Builder':
        """public com.google.common.graph.ImmutableNetwork$Builder<N, E> com.google.common.graph.ImmutableNetwork$Builder.addEdge(com.google.common.graph.EndpointPair<N>,E)"""
        return 'Builder'.__wrap(super(__Builder, self).addEdge(endpoints, edge))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.graph.ImmutableGraph$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.graph.ImmutableGraph as __ImmutableGraph
__ImmutableGraph = __ImmutableGraph
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.google.common.graph.ImmutableGraph as __ImmutableGraph_Builder
__Builder = __ImmutableGraph_Builder.Builder
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Builder():
    """com.google.common.graph.ImmutableGraph.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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

    @overload
    def addNode(self, node: object) -> 'Builder':
        """public com.google.common.graph.ImmutableGraph$Builder<N> com.google.common.graph.ImmutableGraph$Builder.addNode(N)"""
        return 'Builder'.__wrap(super(__Builder, self).addNode(node))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def putEdge(self, endpoints: 'EndpointPair') -> 'Builder':
        """public com.google.common.graph.ImmutableGraph$Builder<N> com.google.common.graph.ImmutableGraph$Builder.putEdge(com.google.common.graph.EndpointPair<N>)"""
        return 'Builder'.__wrap(super(__Builder, self).putEdge(endpoints))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def build(self) -> 'ImmutableGraph':
        """public com.google.common.graph.ImmutableGraph<N> com.google.common.graph.ImmutableGraph$Builder.build()"""
        return 'ImmutableGraph'.__wrap(super(Builder, self).build())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def putEdge(self, nodeU: object, nodeV: object) -> 'Builder':
        """public com.google.common.graph.ImmutableGraph$Builder<N> com.google.common.graph.ImmutableGraph$Builder.putEdge(N,N)"""
        return 'Builder'.__wrap(super(__Builder, self).putEdge(nodeU, nodeV))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.graph.PredecessorsFunction
import com.google.common.graph.PredecessorsFunction as __PredecessorsFunction
__PredecessorsFunction = __PredecessorsFunction
from abc import abstractmethod, ABC
 
class PredecessorsFunction(ABC):
    """com.google.common.graph.PredecessorsFunction"""
 
    @staticmethod
    def __wrap(java_value: __PredecessorsFunction) -> 'PredecessorsFunction':
        return PredecessorsFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PredecessorsFunction):
        """
        Dynamic initializer for PredecessorsFunction.
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
    def predecessors(self, node: object):
        """public abstract java.lang.Iterable<? extends N> com.google.common.graph.PredecessorsFunction.predecessors(N)"""
        pass 
 
 
# CLASS: com.google.common.graph.Traverser
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.graph.Traverser as __Traverser
__Traverser = __Traverser
import java.lang.Integer as __int
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class Traverser(ABC):
    """com.google.common.graph.Traverser"""
 
    @staticmethod
    def __wrap(java_value: __Traverser) -> 'Traverser':
        return Traverser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Traverser):
        """
        Dynamic initializer for Traverser.
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
    def depthFirstPostOrder(self, startNodes: 'Iterable') -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.depthFirstPostOrder(java.lang.Iterable<? extends N>)"""
        return 'Iterable'.__wrap(super(__Traverser, self).depthFirstPostOrder(startNodes))

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
    def depthFirstPostOrder(self, startNode: object) -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.depthFirstPostOrder(N)"""
        return 'Iterable'.__wrap(super(__Traverser, self).depthFirstPostOrder(startNode))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def breadthFirst(self, startNode: object) -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.breadthFirst(N)"""
        return 'Iterable'.__wrap(super(__Traverser, self).breadthFirst(startNode))

    @staticmethod
    @overload
    def forTree(tree: 'SuccessorsFunction') -> 'Traverser':
        """public static <N> com.google.common.graph.Traverser<N> com.google.common.graph.Traverser.forTree(com.google.common.graph.SuccessorsFunction<N>)"""
        return Traverser.__wrap(__Traverser.forTree(tree))

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

    @staticmethod
    @overload
    def forGraph(graph: 'SuccessorsFunction') -> 'Traverser':
        """public static <N> com.google.common.graph.Traverser<N> com.google.common.graph.Traverser.forGraph(com.google.common.graph.SuccessorsFunction<N>)"""
        return Traverser.__wrap(__Traverser.forGraph(graph))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def depthFirstPreOrder(self, startNodes: 'Iterable') -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.depthFirstPreOrder(java.lang.Iterable<? extends N>)"""
        return 'Iterable'.__wrap(super(__Traverser, self).depthFirstPreOrder(startNodes))

    @overload
    def depthFirstPreOrder(self, startNode: object) -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.depthFirstPreOrder(N)"""
        return 'Iterable'.__wrap(super(__Traverser, self).depthFirstPreOrder(startNode))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def breadthFirst(self, startNodes: 'Iterable') -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.breadthFirst(java.lang.Iterable<? extends N>)"""
        return 'Iterable'.__wrap(super(__Traverser, self).breadthFirst(startNodes))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.graph.Graphs
from pyquantum_helper import import_once as __import_once__
import com.google.common.graph.MutableNetwork as __MutableNetwork
__MutableNetwork = __MutableNetwork
from builtins import type
import com.google.common.graph.Graph as __Graph
__Graph = __Graph
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Class as __Class
__Class = __Class
import com.google.common.graph.GraphsBridgeMethods as __GraphsBridgeMethods
__GraphsBridgeMethods = __GraphsBridgeMethods
import com.google.common.graph.MutableGraph as __MutableGraph
__MutableGraph = __MutableGraph
from builtins import bool
import com.google.common.graph.Network as __Network
__Network = __Network
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.google.common.graph.ImmutableGraph as __ImmutableGraph
__ImmutableGraph = __ImmutableGraph
import com.google.common.graph.ValueGraph as __ValueGraph
__ValueGraph = __ValueGraph
import java.util.Set as __Set
__Set = __Set
import java.lang.Iterable as Iterable
import com.google.common.collect.ImmutableSet as __ImmutableSet
__ImmutableSet = __ImmutableSet
import com.google.common.graph.Graphs as __Graphs
__Graphs = __Graphs
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import com.google.common.graph.MutableValueGraph as __MutableValueGraph
__MutableValueGraph = __MutableValueGraph
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class Graphs():
    """com.google.common.graph.Graphs"""
 
    @staticmethod
    def __wrap(java_value: __Graphs) -> 'Graphs':
        return Graphs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Graphs):
        """
        Dynamic initializer for Graphs.
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

    @staticmethod
    @overload
    def hasCycle(network: 'Network') -> bool:
        """public static boolean com.google.common.graph.Graphs.hasCycle(com.google.common.graph.Network<?, ?>)"""
        return bool.__wrap(__Graphs.hasCycle(network))

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

    @staticmethod
    @overload
    def transpose(graph: 'ValueGraph') -> 'ValueGraph':
        """public static <N,V> com.google.common.graph.ValueGraph<N, V> com.google.common.graph.Graphs.transpose(com.google.common.graph.ValueGraph<N, V>)"""
        return ValueGraph.__wrap(__Graphs.transpose(graph))

    @staticmethod
    @overload
    def inducedSubgraph(graph: 'Graph', nodes: 'Iterable') -> 'MutableGraph':
        """public static <N> com.google.common.graph.MutableGraph<N> com.google.common.graph.Graphs.inducedSubgraph(com.google.common.graph.Graph<N>,java.lang.Iterable<? extends N>)"""
        return MutableGraph.__wrap(__Graphs.inducedSubgraph(graph, nodes))

    @staticmethod
    @overload
    def hasCycle(graph: 'Graph') -> bool:
        """public static <N> boolean com.google.common.graph.Graphs.hasCycle(com.google.common.graph.Graph<N>)"""
        return bool.__wrap(__Graphs.hasCycle(graph))

    @staticmethod
    @overload
    def reachableNodes(graph: 'Graph', node: object) -> 'Set':
        """public static <N> java.util.Set<N> com.google.common.graph.GraphsBridgeMethods.reachableNodes(com.google.common.graph.Graph<N>,N)"""
        return Set.__wrap(__GraphsBridgeMethods.reachableNodes(graph, node))

    @staticmethod
    @overload
    def inducedSubgraph(network: 'Network', nodes: 'Iterable') -> 'MutableNetwork':
        """public static <N,E> com.google.common.graph.MutableNetwork<N, E> com.google.common.graph.Graphs.inducedSubgraph(com.google.common.graph.Network<N, E>,java.lang.Iterable<? extends N>)"""
        return MutableNetwork.__wrap(__Graphs.inducedSubgraph(network, nodes))

    @staticmethod
    @overload
    def reachableNodes(graph: 'Graph', node: object) -> 'pygcollect.ImmutableSet':
        """public static <N> com.google.common.collect.ImmutableSet<N> com.google.common.graph.Graphs.reachableNodes(com.google.common.graph.Graph<N>,N)"""
        return pygcollect.ImmutableSet.__wrap(__Graphs.reachableNodes(graph, node))

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

    @staticmethod
    @overload
    def copyOf(network: 'Network') -> 'MutableNetwork':
        """public static <N,E> com.google.common.graph.MutableNetwork<N, E> com.google.common.graph.Graphs.copyOf(com.google.common.graph.Network<N, E>)"""
        return MutableNetwork.__wrap(__Graphs.copyOf(network))

    @staticmethod
    @overload
    def transpose(network: 'Network') -> 'Network':
        """public static <N,E> com.google.common.graph.Network<N, E> com.google.common.graph.Graphs.transpose(com.google.common.graph.Network<N, E>)"""
        return Network.__wrap(__Graphs.transpose(network))

    @staticmethod
    @overload
    def transitiveClosure(graph: 'Graph') -> 'Graph':
        """public static <N> com.google.common.graph.Graph<N> com.google.common.graph.GraphsBridgeMethods.transitiveClosure(com.google.common.graph.Graph<N>)"""
        return Graph.__wrap(__GraphsBridgeMethods.transitiveClosure(graph))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def transpose(graph: 'Graph') -> 'Graph':
        """public static <N> com.google.common.graph.Graph<N> com.google.common.graph.Graphs.transpose(com.google.common.graph.Graph<N>)"""
        return Graph.__wrap(__Graphs.transpose(graph))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def inducedSubgraph(graph: 'ValueGraph', nodes: 'Iterable') -> 'MutableValueGraph':
        """public static <N,V> com.google.common.graph.MutableValueGraph<N, V> com.google.common.graph.Graphs.inducedSubgraph(com.google.common.graph.ValueGraph<N, V>,java.lang.Iterable<? extends N>)"""
        return MutableValueGraph.__wrap(__Graphs.inducedSubgraph(graph, nodes))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def copyOf(graph: 'ValueGraph') -> 'MutableValueGraph':
        """public static <N,V> com.google.common.graph.MutableValueGraph<N, V> com.google.common.graph.Graphs.copyOf(com.google.common.graph.ValueGraph<N, V>)"""
        return MutableValueGraph.__wrap(__Graphs.copyOf(graph))

    @staticmethod
    @overload
    def copyOf(graph: 'Graph') -> 'MutableGraph':
        """public static <N> com.google.common.graph.MutableGraph<N> com.google.common.graph.Graphs.copyOf(com.google.common.graph.Graph<N>)"""
        return MutableGraph.__wrap(__Graphs.copyOf(graph))

    @staticmethod
    @overload
    def transitiveClosure(graph: 'Graph') -> 'ImmutableGraph':
        """public static <N> com.google.common.graph.ImmutableGraph<N> com.google.common.graph.Graphs.transitiveClosure(com.google.common.graph.Graph<N>)"""
        return ImmutableGraph.__wrap(__Graphs.transitiveClosure(graph))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))