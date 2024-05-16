from __future__ import annotations
from overload import overload


 
import com.google.common.graph.PredecessorsFunction as _PredecessorsFunction
_PredecessorsFunction = _PredecessorsFunction
from abc import abstractmethod, ABC
 
class PredecessorsFunction():
    """com.google.common.graph.PredecessorsFunction"""
 
    @staticmethod
    def _wrap(java_value: _PredecessorsFunction) -> 'PredecessorsFunction':
        return PredecessorsFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredecessorsFunction):
        """
        Dynamic initializer for PredecessorsFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredecessorsFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredecessorsFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.lang.Iterable<? extends N> com.google.common.graph.PredecessorsFunction.predecessors(N)"""
        pass

 
 
 
# CLASS: com.google.common.graph.PredecessorsFunction
import com.google.common.graph.PredecessorsFunction as _PredecessorsFunction
_PredecessorsFunction = _PredecessorsFunction
from abc import abstractmethod, ABC
 
class PredecessorsFunction():
    """com.google.common.graph.PredecessorsFunction"""
 
    @staticmethod
    def _wrap(java_value: _PredecessorsFunction) -> 'PredecessorsFunction':
        return PredecessorsFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PredecessorsFunction):
        """
        Dynamic initializer for PredecessorsFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PredecessorsFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PredecessorsFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.lang.Iterable<? extends N> com.google.common.graph.PredecessorsFunction.predecessors(N)"""
        pass

 
 
 
# CLASS: com.google.common.graph.PredecessorsFunction 
 
 
# CLASS: com.google.common.graph.SuccessorsFunction
import com.google.common.graph.SuccessorsFunction as _SuccessorsFunction
_SuccessorsFunction = _SuccessorsFunction
from abc import abstractmethod, ABC
 
class SuccessorsFunction():
    """com.google.common.graph.SuccessorsFunction"""
 
    @staticmethod
    def _wrap(java_value: _SuccessorsFunction) -> 'SuccessorsFunction':
        return SuccessorsFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SuccessorsFunction):
        """
        Dynamic initializer for SuccessorsFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SuccessorsFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SuccessorsFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def successors(self, node: object):
        """public abstract java.lang.Iterable<? extends N> com.google.common.graph.SuccessorsFunction.successors(N)"""
        pass 
 
 
# CLASS: com.google.common.graph.MutableValueGraph
import com.google.common.graph.MutableValueGraph as _MutableValueGraph
_MutableValueGraph = _MutableValueGraph
from abc import abstractmethod, ABC
import com.google.common.graph.ValueGraph as _ValueGraph
_ValueGraph = _ValueGraph
 
class MutableValueGraph():
    """com.google.common.graph.MutableValueGraph"""
 
    @staticmethod
    def _wrap(java_value: _MutableValueGraph) -> 'MutableValueGraph':
        return MutableValueGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableValueGraph):
        """
        Dynamic initializer for MutableValueGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableValueGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableValueGraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.graph.ElementOrder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import com.google.common.graph.ElementOrder as _ElementOrder_Type
_Type = _ElementOrder_Type.Type
import com.google.common.graph.ElementOrder as _ElementOrder
_ElementOrder = _ElementOrder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ElementOrder():
    """com.google.common.graph.ElementOrder"""
 
    @staticmethod
    def _wrap(java_value: _ElementOrder) -> 'ElementOrder':
        return ElementOrder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ElementOrder):
        """
        Dynamic initializer for ElementOrder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ElementOrder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ElementOrder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def insertion() -> 'ElementOrder':
        """public static <S> com.google.common.graph.ElementOrder<S> com.google.common.graph.ElementOrder.insertion()"""
        return ElementOrder._wrap(_ElementOrder.insertion())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.graph.ElementOrder.hashCode()"""
        return int._wrap(super(ElementOrder, self).hashCode())

    @staticmethod
    @overload
    def natural() -> 'ElementOrder':
        """public static <S extends java.lang.Comparable<? super S>> com.google.common.graph.ElementOrder<S> com.google.common.graph.ElementOrder.natural()"""
        return ElementOrder._wrap(_ElementOrder.natural())

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.graph.ElementOrder.equals(java.lang.Object)"""
        return bool._wrap(super(_ElementOrder, self).equals(obj))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def type(self) -> 'Type':
        """public com.google.common.graph.ElementOrder$Type com.google.common.graph.ElementOrder.type()"""
        return 'Type'._wrap(super(ElementOrder, self).type())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def comparator(self) -> 'Comparator':
        """public java.util.Comparator<T> com.google.common.graph.ElementOrder.comparator()"""
        return 'Comparator'._wrap(super(ElementOrder, self).comparator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.ElementOrder.toString()"""
        return str._wrap(super(ElementOrder, self).toString())

    @staticmethod
    @overload
    def sorted(comparator: 'Comparator') -> 'ElementOrder':
        """public static <S> com.google.common.graph.ElementOrder<S> com.google.common.graph.ElementOrder.sorted(java.util.Comparator<S>)"""
        return ElementOrder._wrap(_ElementOrder.sorted(comparator))

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

    @staticmethod
    @overload
    def unordered() -> 'ElementOrder':
        """public static <S> com.google.common.graph.ElementOrder<S> com.google.common.graph.ElementOrder.unordered()"""
        return ElementOrder._wrap(_ElementOrder.unordered())

    @staticmethod
    @overload
    def stable() -> 'ElementOrder':
        """public static <S> com.google.common.graph.ElementOrder<S> com.google.common.graph.ElementOrder.stable()"""
        return ElementOrder._wrap(_ElementOrder.stable())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.graph.Network
import com.google.common.graph.Network as _Network
_Network = _Network
from abc import abstractmethod, ABC
 
class Network():
    """com.google.common.graph.Network"""
 
    @staticmethod
    def _wrap(java_value: _Network) -> 'Network':
        return Network(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Network):
        """
        Dynamic initializer for Network.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Network__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Network__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.graph.ValueGraphBuilder
from builtins import str
from pyquantum_helper import override
import com.google.common.graph.ImmutableValueGraph as _ImmutableValueGraph_Builder
_Builder = _ImmutableValueGraph_Builder.Builder
import java.lang.Object as _Object
_Object = _Object
import com.google.common.graph.MutableValueGraph as _MutableValueGraph
_MutableValueGraph = _MutableValueGraph
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.graph.ValueGraphBuilder as _ValueGraphBuilder
_ValueGraphBuilder = _ValueGraphBuilder
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ValueGraphBuilder():
    """com.google.common.graph.ValueGraphBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ValueGraphBuilder) -> 'ValueGraphBuilder':
        return ValueGraphBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValueGraphBuilder):
        """
        Dynamic initializer for ValueGraphBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValueGraphBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValueGraphBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def incidentEdgeOrder(self, incidentEdgeOrder: 'ElementOrder') -> 'ValueGraphBuilder':
        """public <N1 extends N> com.google.common.graph.ValueGraphBuilder<N1, V> com.google.common.graph.ValueGraphBuilder.incidentEdgeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'ValueGraphBuilder'._wrap(super(_ValueGraphBuilder, self).incidentEdgeOrder(incidentEdgeOrder))

    @overload
    def build(self) -> 'MutableValueGraph':
        """public <N1 extends N,V1 extends V> com.google.common.graph.MutableValueGraph<N1, V1> com.google.common.graph.ValueGraphBuilder.build()"""
        return 'MutableValueGraph'._wrap(super(ValueGraphBuilder, self).build())

    @staticmethod
    @overload
    def from(graph: 'ValueGraph') -> 'ValueGraphBuilder':
        """public static <N,V> com.google.common.graph.ValueGraphBuilder<N, V> com.google.common.graph.ValueGraphBuilder.from(com.google.common.graph.ValueGraph<N, V>)"""
        return ValueGraphBuilder._wrap(_ValueGraphBuilder.from(graph))

    @overload
    def allowsSelfLoops(self, allowsSelfLoops: bool) -> 'ValueGraphBuilder':
        """public com.google.common.graph.ValueGraphBuilder<N, V> com.google.common.graph.ValueGraphBuilder.allowsSelfLoops(boolean)"""
        return 'ValueGraphBuilder'._wrap(super(_ValueGraphBuilder, self).allowsSelfLoops(_boolean.valueOf(allowsSelfLoops)))

    @overload
    def nodeOrder(self, nodeOrder: 'ElementOrder') -> 'ValueGraphBuilder':
        """public <N1 extends N> com.google.common.graph.ValueGraphBuilder<N1, V> com.google.common.graph.ValueGraphBuilder.nodeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'ValueGraphBuilder'._wrap(super(_ValueGraphBuilder, self).nodeOrder(nodeOrder))

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

    @staticmethod
    @overload
    def undirected() -> 'ValueGraphBuilder':
        """public static com.google.common.graph.ValueGraphBuilder<java.lang.Object, java.lang.Object> com.google.common.graph.ValueGraphBuilder.undirected()"""
        return ValueGraphBuilder._wrap(_ValueGraphBuilder.undirected())

    @overload
    def immutable(self) -> 'Builder':
        """public <N1 extends N,V1 extends V> com.google.common.graph.ImmutableValueGraph$Builder<N1, V1> com.google.common.graph.ValueGraphBuilder.immutable()"""
        return 'Builder'._wrap(super(ValueGraphBuilder, self).immutable())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def directed() -> 'ValueGraphBuilder':
        """public static com.google.common.graph.ValueGraphBuilder<java.lang.Object, java.lang.Object> com.google.common.graph.ValueGraphBuilder.directed()"""
        return ValueGraphBuilder._wrap(_ValueGraphBuilder.directed())

    @overload
    def expectedNodeCount(self, expectedNodeCount: int) -> 'ValueGraphBuilder':
        """public com.google.common.graph.ValueGraphBuilder<N, V> com.google.common.graph.ValueGraphBuilder.expectedNodeCount(int)"""
        return 'ValueGraphBuilder'._wrap(super(_ValueGraphBuilder, self).expectedNodeCount(_int.valueOf(expectedNodeCount)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.graph.NetworkBuilder
import com.google.common.graph.NetworkBuilder as _NetworkBuilder
_NetworkBuilder = _NetworkBuilder
from builtins import str
from pyquantum_helper import override
import com.google.common.graph.ImmutableNetwork as _ImmutableNetwork_Builder
_Builder = _ImmutableNetwork_Builder.Builder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.graph.MutableNetwork as _MutableNetwork
_MutableNetwork = _MutableNetwork
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NetworkBuilder():
    """com.google.common.graph.NetworkBuilder"""
 
    @staticmethod
    def _wrap(java_value: _NetworkBuilder) -> 'NetworkBuilder':
        return NetworkBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NetworkBuilder):
        """
        Dynamic initializer for NetworkBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NetworkBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NetworkBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def allowsSelfLoops(self, allowsSelfLoops: bool) -> 'NetworkBuilder':
        """public com.google.common.graph.NetworkBuilder<N, E> com.google.common.graph.NetworkBuilder.allowsSelfLoops(boolean)"""
        return 'NetworkBuilder'._wrap(super(_NetworkBuilder, self).allowsSelfLoops(_boolean.valueOf(allowsSelfLoops)))

    @overload
    def nodeOrder(self, nodeOrder: 'ElementOrder') -> 'NetworkBuilder':
        """public <N1 extends N> com.google.common.graph.NetworkBuilder<N1, E> com.google.common.graph.NetworkBuilder.nodeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'NetworkBuilder'._wrap(super(_NetworkBuilder, self).nodeOrder(nodeOrder))

    @staticmethod
    @overload
    def directed() -> 'NetworkBuilder':
        """public static com.google.common.graph.NetworkBuilder<java.lang.Object, java.lang.Object> com.google.common.graph.NetworkBuilder.directed()"""
        return NetworkBuilder._wrap(_NetworkBuilder.directed())

    @overload
    def allowsParallelEdges(self, allowsParallelEdges: bool) -> 'NetworkBuilder':
        """public com.google.common.graph.NetworkBuilder<N, E> com.google.common.graph.NetworkBuilder.allowsParallelEdges(boolean)"""
        return 'NetworkBuilder'._wrap(super(_NetworkBuilder, self).allowsParallelEdges(_boolean.valueOf(allowsParallelEdges)))

    @overload
    def expectedNodeCount(self, expectedNodeCount: int) -> 'NetworkBuilder':
        """public com.google.common.graph.NetworkBuilder<N, E> com.google.common.graph.NetworkBuilder.expectedNodeCount(int)"""
        return 'NetworkBuilder'._wrap(super(_NetworkBuilder, self).expectedNodeCount(_int.valueOf(expectedNodeCount)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def expectedEdgeCount(self, expectedEdgeCount: int) -> 'NetworkBuilder':
        """public com.google.common.graph.NetworkBuilder<N, E> com.google.common.graph.NetworkBuilder.expectedEdgeCount(int)"""
        return 'NetworkBuilder'._wrap(super(_NetworkBuilder, self).expectedEdgeCount(_int.valueOf(expectedEdgeCount)))

    @overload
    def edgeOrder(self, edgeOrder: 'ElementOrder') -> 'NetworkBuilder':
        """public <E1 extends E> com.google.common.graph.NetworkBuilder<N, E1> com.google.common.graph.NetworkBuilder.edgeOrder(com.google.common.graph.ElementOrder<E1>)"""
        return 'NetworkBuilder'._wrap(super(_NetworkBuilder, self).edgeOrder(edgeOrder))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def undirected() -> 'NetworkBuilder':
        """public static com.google.common.graph.NetworkBuilder<java.lang.Object, java.lang.Object> com.google.common.graph.NetworkBuilder.undirected()"""
        return NetworkBuilder._wrap(_NetworkBuilder.undirected())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def from(network: 'Network') -> 'NetworkBuilder':
        """public static <N,E> com.google.common.graph.NetworkBuilder<N, E> com.google.common.graph.NetworkBuilder.from(com.google.common.graph.Network<N, E>)"""
        return NetworkBuilder._wrap(_NetworkBuilder.from(network))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def immutable(self) -> 'Builder':
        """public <N1 extends N,E1 extends E> com.google.common.graph.ImmutableNetwork$Builder<N1, E1> com.google.common.graph.NetworkBuilder.immutable()"""
        return 'Builder'._wrap(super(NetworkBuilder, self).immutable())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def build(self) -> 'MutableNetwork':
        """public <N1 extends N,E1 extends E> com.google.common.graph.MutableNetwork<N1, E1> com.google.common.graph.NetworkBuilder.build()"""
        return 'MutableNetwork'._wrap(super(NetworkBuilder, self).build())

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
 
 
# CLASS: com.google.common.graph.ValueGraph
import com.google.common.graph.ValueGraph as _ValueGraph
_ValueGraph = _ValueGraph
from abc import abstractmethod, ABC
 
class ValueGraph():
    """com.google.common.graph.ValueGraph"""
 
    @staticmethod
    def _wrap(java_value: _ValueGraph) -> 'ValueGraph':
        return ValueGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValueGraph):
        """
        Dynamic initializer for ValueGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValueGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValueGraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.graph.GraphBuilder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.graph.ImmutableGraph as _ImmutableGraph_Builder
_Builder = _ImmutableGraph_Builder.Builder
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.google.common.graph.MutableGraph as _MutableGraph
_MutableGraph = _MutableGraph
import com.google.common.graph.GraphBuilder as _GraphBuilder
_GraphBuilder = _GraphBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GraphBuilder():
    """com.google.common.graph.GraphBuilder"""
 
    @staticmethod
    def _wrap(java_value: _GraphBuilder) -> 'GraphBuilder':
        return GraphBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GraphBuilder):
        """
        Dynamic initializer for GraphBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GraphBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GraphBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def immutable(self) -> 'Builder':
        """public <N1 extends N> com.google.common.graph.ImmutableGraph$Builder<N1> com.google.common.graph.GraphBuilder.immutable()"""
        return 'Builder'._wrap(super(GraphBuilder, self).immutable())

    @staticmethod
    @overload
    def undirected() -> 'GraphBuilder':
        """public static com.google.common.graph.GraphBuilder<java.lang.Object> com.google.common.graph.GraphBuilder.undirected()"""
        return GraphBuilder._wrap(_GraphBuilder.undirected())

    @staticmethod
    @overload
    def directed() -> 'GraphBuilder':
        """public static com.google.common.graph.GraphBuilder<java.lang.Object> com.google.common.graph.GraphBuilder.directed()"""
        return GraphBuilder._wrap(_GraphBuilder.directed())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def from(graph: 'Graph') -> 'GraphBuilder':
        """public static <N> com.google.common.graph.GraphBuilder<N> com.google.common.graph.GraphBuilder.from(com.google.common.graph.Graph<N>)"""
        return GraphBuilder._wrap(_GraphBuilder.from(graph))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def build(self) -> 'MutableGraph':
        """public <N1 extends N> com.google.common.graph.MutableGraph<N1> com.google.common.graph.GraphBuilder.build()"""
        return 'MutableGraph'._wrap(super(GraphBuilder, self).build())

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
    def allowsSelfLoops(self, allowsSelfLoops: bool) -> 'GraphBuilder':
        """public com.google.common.graph.GraphBuilder<N> com.google.common.graph.GraphBuilder.allowsSelfLoops(boolean)"""
        return 'GraphBuilder'._wrap(super(_GraphBuilder, self).allowsSelfLoops(_boolean.valueOf(allowsSelfLoops)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def nodeOrder(self, nodeOrder: 'ElementOrder') -> 'GraphBuilder':
        """public <N1 extends N> com.google.common.graph.GraphBuilder<N1> com.google.common.graph.GraphBuilder.nodeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'GraphBuilder'._wrap(super(_GraphBuilder, self).nodeOrder(nodeOrder))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def expectedNodeCount(self, expectedNodeCount: int) -> 'GraphBuilder':
        """public com.google.common.graph.GraphBuilder<N> com.google.common.graph.GraphBuilder.expectedNodeCount(int)"""
        return 'GraphBuilder'._wrap(super(_GraphBuilder, self).expectedNodeCount(_int.valueOf(expectedNodeCount)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def incidentEdgeOrder(self, incidentEdgeOrder: 'ElementOrder') -> 'GraphBuilder':
        """public <N1 extends N> com.google.common.graph.GraphBuilder<N1> com.google.common.graph.GraphBuilder.incidentEdgeOrder(com.google.common.graph.ElementOrder<N1>)"""
        return 'GraphBuilder'._wrap(super(_GraphBuilder, self).incidentEdgeOrder(incidentEdgeOrder))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.graph.AbstractGraph
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.google.common.graph.AbstractGraph as _AbstractGraph
_AbstractGraph = _AbstractGraph
import java.lang.Integer as _int
import com.google.common.graph.Graph as _Graph
_Graph = _Graph
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractGraph():
    """com.google.common.graph.AbstractGraph"""
 
    @staticmethod
    def _wrap(java_value: _AbstractGraph) -> 'AbstractGraph':
        return AbstractGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractGraph):
        """
        Dynamic initializer for AbstractGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractGraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.google.common.graph.AbstractGraph()"""
        val = _AbstractGraph()
        self.__wrapper = val

    @abstractmethod
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.Graph.isDirected()"""
        pass

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.predecessors(N)"""
        pass

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.nodes()"""
        pass

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractGraph.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractGraph, self).equals(obj))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Graph.successors(N)"""
        pass

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
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractGraph.hashCode()"""
        return int._wrap(super(AbstractGraph, self).hashCode())

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.Graph.allowsSelfLoops()"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractGraph.toString()"""
        return str._wrap(super(AbstractGraph, self).toString())

    @overload
    def __init__(self):
        """public com.google.common.graph.AbstractGraph()"""
        val = _AbstractGraph()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.graph.ImmutableNetwork$Builder
from builtins import str
from pyquantum_helper import override
import com.google.common.graph.ImmutableNetwork as _ImmutableNetwork_Builder
_Builder = _ImmutableNetwork_Builder.Builder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.graph.ImmutableNetwork as _ImmutableNetwork
_ImmutableNetwork = _ImmutableNetwork
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """com.google.common.graph.ImmutableNetwork.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def build(self) -> 'ImmutableNetwork':
        """public com.google.common.graph.ImmutableNetwork<N, E> com.google.common.graph.ImmutableNetwork$Builder.build()"""
        return 'ImmutableNetwork'._wrap(super(Builder, self).build())

    @overload
    def addNode(self, node: object) -> 'Builder':
        """public com.google.common.graph.ImmutableNetwork$Builder<N, E> com.google.common.graph.ImmutableNetwork$Builder.addNode(N)"""
        return 'Builder'._wrap(super(_Builder, self).addNode(node))

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
    def addEdge(self, nodeU: object, nodeV: object, edge: object) -> 'Builder':
        """public com.google.common.graph.ImmutableNetwork$Builder<N, E> com.google.common.graph.ImmutableNetwork$Builder.addEdge(N,N,E)"""
        return 'Builder'._wrap(super(_Builder, self).addEdge(nodeU, nodeV, edge))

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
    def addEdge(self, endpoints: 'EndpointPair', edge: object) -> 'Builder':
        """public com.google.common.graph.ImmutableNetwork$Builder<N, E> com.google.common.graph.ImmutableNetwork$Builder.addEdge(com.google.common.graph.EndpointPair<N>,E)"""
        return 'Builder'._wrap(super(_Builder, self).addEdge(endpoints, edge))

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
 
 
# CLASS: com.google.common.graph.ImmutableValueGraph
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.graph.ImmutableValueGraph as _ImmutableValueGraph
_ImmutableValueGraph = _ImmutableValueGraph
import com.google.common.graph.ImmutableGraph as _ImmutableGraph
_ImmutableGraph = _ImmutableGraph
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import com.google.common.graph.ElementOrder as _ElementOrder
_ElementOrder = _ElementOrder
import com.google.common.graph.AbstractValueGraph as _AbstractValueGraph
_AbstractValueGraph = _AbstractValueGraph
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImmutableValueGraph():
    """com.google.common.graph.ImmutableValueGraph"""
 
    @staticmethod
    def _wrap(java_value: _ImmutableValueGraph) -> 'ImmutableValueGraph':
        return ImmutableValueGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmutableValueGraph):
        """
        Dynamic initializer for ImmutableValueGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmutableValueGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmutableValueGraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def edgeValue(self, nodeU: object, nodeV: object) -> 'Optional':
        """public java.util.Optional<V> com.google.common.graph.AbstractValueGraph.edgeValue(N,N)"""
        return 'Optional'._wrap(super(_AbstractValueGraph, self).edgeValue(nodeU, nodeV))

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

    @staticmethod
    @overload
    def copyOf(graph: 'ImmutableValueGraph') -> 'ImmutableValueGraph':
        """public static <N,V> com.google.common.graph.ImmutableValueGraph<N, V> com.google.common.graph.ImmutableValueGraph.copyOf(com.google.common.graph.ImmutableValueGraph<N, V>)"""
        return ImmutableValueGraph._wrap(_ImmutableValueGraph.copyOf(graph))

    @override
    @overload
    def incidentEdgeOrder(self) -> 'ElementOrder':
        """public com.google.common.graph.ElementOrder<N> com.google.common.graph.ImmutableValueGraph.incidentEdgeOrder()"""
        return 'ElementOrder'._wrap(super(ImmutableValueGraph, self).incidentEdgeOrder())

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
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractValueGraph.toString()"""
        return str._wrap(super(AbstractValueGraph, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def asGraph(self) -> 'ImmutableGraph':
        """public com.google.common.graph.ImmutableGraph<N> com.google.common.graph.ImmutableValueGraph.asGraph()"""
        return 'ImmutableGraph'._wrap(super(ImmutableValueGraph, self).asGraph())

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractValueGraph.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractValueGraph, self).equals(obj))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def copyOf(graph: 'ValueGraph') -> 'ImmutableValueGraph':
        """public static <N,V> com.google.common.graph.ImmutableValueGraph<N, V> com.google.common.graph.ImmutableValueGraph.copyOf(com.google.common.graph.ValueGraph<N, V>)"""
        return ImmutableValueGraph._wrap(_ImmutableValueGraph.copyOf(graph))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractValueGraph.hashCode()"""
        return int._wrap(super(AbstractValueGraph, self).hashCode())

    @overload
    def edgeValue(self, endpoints: 'EndpointPair') -> 'Optional':
        """public java.util.Optional<V> com.google.common.graph.AbstractValueGraph.edgeValue(com.google.common.graph.EndpointPair<N>)"""
        return 'Optional'._wrap(super(_AbstractValueGraph, self).edgeValue(endpoints)) 
 
 
# CLASS: com.google.common.graph.Graphs
from pyquantum_helper import import_once as _import_once
import com.google.common.graph.Graphs as _Graphs
_Graphs = _Graphs
import java.lang.Object as _Object
_Object = _Object
import com.google.common.graph.MutableValueGraph as _MutableValueGraph
_MutableValueGraph = _MutableValueGraph
from builtins import type
import com.google.common.graph.ValueGraph as _ValueGraph
_ValueGraph = _ValueGraph
import java.util.Set as _Set
_Set = _Set
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import com.google.common.collect.ImmutableSet as _ImmutableSet
_ImmutableSet = _ImmutableSet
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.Iterable as Iterable
import com.google.common.graph.Network as _Network
_Network = _Network
import java.lang.String as _String
_String = _String
import com.google.common.graph.MutableNetwork as _MutableNetwork
_MutableNetwork = _MutableNetwork
import java.util.Set as Set
import com.google.common.graph.ImmutableGraph as _ImmutableGraph
_ImmutableGraph = _ImmutableGraph
import com.google.common.graph.Graph as _Graph
_Graph = _Graph
import java.lang.Integer as _int
import com.google.common.graph.MutableGraph as _MutableGraph
_MutableGraph = _MutableGraph
import com.google.common.graph.GraphsBridgeMethods as _GraphsBridgeMethods
_GraphsBridgeMethods = _GraphsBridgeMethods
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Graphs():
    """com.google.common.graph.Graphs"""
 
    @staticmethod
    def _wrap(java_value: _Graphs) -> 'Graphs':
        return Graphs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Graphs):
        """
        Dynamic initializer for Graphs.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Graphs__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Graphs__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def inducedSubgraph(network: 'Network', nodes: 'Iterable') -> 'MutableNetwork':
        """public static <N,E> com.google.common.graph.MutableNetwork<N, E> com.google.common.graph.Graphs.inducedSubgraph(com.google.common.graph.Network<N, E>,java.lang.Iterable<? extends N>)"""
        return MutableNetwork._wrap(_Graphs.inducedSubgraph(network, nodes))

    @staticmethod
    @overload
    def inducedSubgraph(graph: 'ValueGraph', nodes: 'Iterable') -> 'MutableValueGraph':
        """public static <N,V> com.google.common.graph.MutableValueGraph<N, V> com.google.common.graph.Graphs.inducedSubgraph(com.google.common.graph.ValueGraph<N, V>,java.lang.Iterable<? extends N>)"""
        return MutableValueGraph._wrap(_Graphs.inducedSubgraph(graph, nodes))

    @staticmethod
    @overload
    def hasCycle(graph: 'Graph') -> bool:
        """public static <N> boolean com.google.common.graph.Graphs.hasCycle(com.google.common.graph.Graph<N>)"""
        return bool._wrap(_Graphs.hasCycle(graph))

    @staticmethod
    @overload
    def transpose(graph: 'ValueGraph') -> 'ValueGraph':
        """public static <N,V> com.google.common.graph.ValueGraph<N, V> com.google.common.graph.Graphs.transpose(com.google.common.graph.ValueGraph<N, V>)"""
        return ValueGraph._wrap(_Graphs.transpose(graph))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def transitiveClosure(graph: 'Graph') -> 'ImmutableGraph':
        """public static <N> com.google.common.graph.ImmutableGraph<N> com.google.common.graph.Graphs.transitiveClosure(com.google.common.graph.Graph<N>)"""
        return ImmutableGraph._wrap(_Graphs.transitiveClosure(graph))

    @staticmethod
    @overload
    def copyOf(graph: 'Graph') -> 'MutableGraph':
        """public static <N> com.google.common.graph.MutableGraph<N> com.google.common.graph.Graphs.copyOf(com.google.common.graph.Graph<N>)"""
        return MutableGraph._wrap(_Graphs.copyOf(graph))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def transpose(network: 'Network') -> 'Network':
        """public static <N,E> com.google.common.graph.Network<N, E> com.google.common.graph.Graphs.transpose(com.google.common.graph.Network<N, E>)"""
        return Network._wrap(_Graphs.transpose(network))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def copyOf(network: 'Network') -> 'MutableNetwork':
        """public static <N,E> com.google.common.graph.MutableNetwork<N, E> com.google.common.graph.Graphs.copyOf(com.google.common.graph.Network<N, E>)"""
        return MutableNetwork._wrap(_Graphs.copyOf(network))

    @staticmethod
    @overload
    def inducedSubgraph(graph: 'Graph', nodes: 'Iterable') -> 'MutableGraph':
        """public static <N> com.google.common.graph.MutableGraph<N> com.google.common.graph.Graphs.inducedSubgraph(com.google.common.graph.Graph<N>,java.lang.Iterable<? extends N>)"""
        return MutableGraph._wrap(_Graphs.inducedSubgraph(graph, nodes))

    @staticmethod
    @overload
    def hasCycle(network: 'Network') -> bool:
        """public static boolean com.google.common.graph.Graphs.hasCycle(com.google.common.graph.Network<?, ?>)"""
        return bool._wrap(_Graphs.hasCycle(network))

    @staticmethod
    @overload
    def reachableNodes(graph: 'Graph', node: object) -> 'pygcollect.ImmutableSet':
        """public static <N> com.google.common.collect.ImmutableSet<N> com.google.common.graph.Graphs.reachableNodes(com.google.common.graph.Graph<N>,N)"""
        return pygcollect.ImmutableSet._wrap(_Graphs.reachableNodes(graph, node))

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

    @staticmethod
    @overload
    def transitiveClosure(graph: 'Graph') -> 'Graph':
        """public static <N> com.google.common.graph.Graph<N> com.google.common.graph.GraphsBridgeMethods.transitiveClosure(com.google.common.graph.Graph<N>)"""
        return Graph._wrap(_GraphsBridgeMethods.transitiveClosure(graph))

    @staticmethod
    @overload
    def transpose(graph: 'Graph') -> 'Graph':
        """public static <N> com.google.common.graph.Graph<N> com.google.common.graph.Graphs.transpose(com.google.common.graph.Graph<N>)"""
        return Graph._wrap(_Graphs.transpose(graph))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def reachableNodes(graph: 'Graph', node: object) -> 'Set':
        """public static <N> java.util.Set<N> com.google.common.graph.GraphsBridgeMethods.reachableNodes(com.google.common.graph.Graph<N>,N)"""
        return Set._wrap(_GraphsBridgeMethods.reachableNodes(graph, node))

    @staticmethod
    @overload
    def copyOf(graph: 'ValueGraph') -> 'MutableValueGraph':
        """public static <N,V> com.google.common.graph.MutableValueGraph<N, V> com.google.common.graph.Graphs.copyOf(com.google.common.graph.ValueGraph<N, V>)"""
        return MutableValueGraph._wrap(_Graphs.copyOf(graph))

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
 
 
# CLASS: com.google.common.graph.ImmutableNetwork
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.graph.AbstractNetwork as _AbstractNetwork
_AbstractNetwork = _AbstractNetwork
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.Set as _Set
_Set = _Set
import com.google.common.graph.ImmutableNetwork as _ImmutableNetwork
_ImmutableNetwork = _ImmutableNetwork
import java.util.Set as Set
import com.google.common.graph.ImmutableGraph as _ImmutableGraph
_ImmutableGraph = _ImmutableGraph
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImmutableNetwork():
    """com.google.common.graph.ImmutableNetwork"""
 
    @staticmethod
    def _wrap(java_value: _ImmutableNetwork) -> 'ImmutableNetwork':
        return ImmutableNetwork(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmutableNetwork):
        """
        Dynamic initializer for ImmutableNetwork.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmutableNetwork__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmutableNetwork__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def copyOf(network: 'ImmutableNetwork') -> 'ImmutableNetwork':
        """public static <N,E> com.google.common.graph.ImmutableNetwork<N, E> com.google.common.graph.ImmutableNetwork.copyOf(com.google.common.graph.ImmutableNetwork<N, E>)"""
        return ImmutableNetwork._wrap(_ImmutableNetwork.copyOf(network))

    @overload
    def edgesConnecting(self, endpoints: 'EndpointPair') -> 'Set':
        """public java.util.Set<E> com.google.common.graph.AbstractNetwork.edgesConnecting(com.google.common.graph.EndpointPair<N>)"""
        return 'Set'._wrap(super(_AbstractNetwork, self).edgesConnecting(endpoints))

    @overload
    def outDegree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.outDegree(N)"""
        return int._wrap(super(_AbstractNetwork, self).outDegree(node))

    @overload
    def edgeConnectingOrNull(self, nodeU: object, nodeV: object) -> object:
        """public E com.google.common.graph.AbstractNetwork.edgeConnectingOrNull(N,N)"""
        return object._wrap(super(_AbstractNetwork, self).edgeConnectingOrNull(nodeU, nodeV))

    @override
    @overload
    def asGraph(self) -> 'ImmutableGraph':
        """public com.google.common.graph.ImmutableGraph<N> com.google.common.graph.ImmutableNetwork.asGraph()"""
        return 'ImmutableGraph'._wrap(super(ImmutableNetwork, self).asGraph())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractNetwork.toString()"""
        return str._wrap(super(AbstractNetwork, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractNetwork.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractNetwork, self).equals(obj))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractNetwork.hashCode()"""
        return int._wrap(super(AbstractNetwork, self).hashCode())

    @staticmethod
    @overload
    def copyOf(network: 'Network') -> 'ImmutableNetwork':
        """public static <N,E> com.google.common.graph.ImmutableNetwork<N, E> com.google.common.graph.ImmutableNetwork.copyOf(com.google.common.graph.Network<N, E>)"""
        return ImmutableNetwork._wrap(_ImmutableNetwork.copyOf(network))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def edgeConnectingOrNull(self, endpoints: 'EndpointPair') -> object:
        """public E com.google.common.graph.AbstractNetwork.edgeConnectingOrNull(com.google.common.graph.EndpointPair<N>)"""
        return object._wrap(super(_AbstractNetwork, self).edgeConnectingOrNull(endpoints))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def edgeConnecting(self, endpoints: 'EndpointPair') -> 'Optional':
        """public java.util.Optional<E> com.google.common.graph.AbstractNetwork.edgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        return 'Optional'._wrap(super(_AbstractNetwork, self).edgeConnecting(endpoints))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def inDegree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.inDegree(N)"""
        return int._wrap(super(_AbstractNetwork, self).inDegree(node))

    @overload
    def adjacentEdges(self, edge: object) -> 'Set':
        """public java.util.Set<E> com.google.common.graph.AbstractNetwork.adjacentEdges(E)"""
        return 'Set'._wrap(super(_AbstractNetwork, self).adjacentEdges(edge))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def edgeConnecting(self, nodeU: object, nodeV: object) -> 'Optional':
        """public java.util.Optional<E> com.google.common.graph.AbstractNetwork.edgeConnecting(N,N)"""
        return 'Optional'._wrap(super(_AbstractNetwork, self).edgeConnecting(nodeU, nodeV))

    @overload
    def hasEdgeConnecting(self, endpoints: 'EndpointPair') -> bool:
        """public boolean com.google.common.graph.AbstractNetwork.hasEdgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        return bool._wrap(super(_AbstractNetwork, self).hasEdgeConnecting(endpoints))

    @overload
    def hasEdgeConnecting(self, nodeU: object, nodeV: object) -> bool:
        """public boolean com.google.common.graph.AbstractNetwork.hasEdgeConnecting(N,N)"""
        return bool._wrap(super(_AbstractNetwork, self).hasEdgeConnecting(nodeU, nodeV))

    @overload
    def degree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.degree(N)"""
        return int._wrap(super(_AbstractNetwork, self).degree(node)) 
 
 
# CLASS: com.google.common.graph.MutableGraph
import com.google.common.graph.Graph as _Graph
_Graph = _Graph
import com.google.common.graph.MutableGraph as _MutableGraph
_MutableGraph = _MutableGraph
from abc import abstractmethod, ABC
 
class MutableGraph():
    """com.google.common.graph.MutableGraph"""
 
    @staticmethod
    def _wrap(java_value: _MutableGraph) -> 'MutableGraph':
        return MutableGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableGraph):
        """
        Dynamic initializer for MutableGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableGraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.graph.ImmutableGraph
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.graph.ImmutableGraph as _ImmutableGraph
_ImmutableGraph = _ImmutableGraph
import com.google.common.graph.AbstractGraph as _AbstractGraph
_AbstractGraph = _AbstractGraph
import java.lang.Integer as _int
import com.google.common.graph.ElementOrder as _ElementOrder
_ElementOrder = _ElementOrder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImmutableGraph():
    """com.google.common.graph.ImmutableGraph"""
 
    @staticmethod
    def _wrap(java_value: _ImmutableGraph) -> 'ImmutableGraph':
        return ImmutableGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmutableGraph):
        """
        Dynamic initializer for ImmutableGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmutableGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmutableGraph__wrapper":
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

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractGraph.hashCode()"""
        return int._wrap(super(AbstractGraph, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def incidentEdgeOrder(self) -> 'ElementOrder':
        """public com.google.common.graph.ElementOrder<N> com.google.common.graph.ImmutableGraph.incidentEdgeOrder()"""
        return 'ElementOrder'._wrap(super(ImmutableGraph, self).incidentEdgeOrder())

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractGraph.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractGraph, self).equals(obj))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractGraph.toString()"""
        return str._wrap(super(AbstractGraph, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def copyOf(graph: 'ImmutableGraph') -> 'ImmutableGraph':
        """public static <N> com.google.common.graph.ImmutableGraph<N> com.google.common.graph.ImmutableGraph.copyOf(com.google.common.graph.ImmutableGraph<N>)"""
        return ImmutableGraph._wrap(_ImmutableGraph.copyOf(graph))

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

    @staticmethod
    @overload
    def copyOf(graph: 'Graph') -> 'ImmutableGraph':
        """public static <N> com.google.common.graph.ImmutableGraph<N> com.google.common.graph.ImmutableGraph.copyOf(com.google.common.graph.Graph<N>)"""
        return ImmutableGraph._wrap(_ImmutableGraph.copyOf(graph)) 
 
 
# CLASS: com.google.common.graph.AbstractNetwork
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.graph.AbstractNetwork as _AbstractNetwork
_AbstractNetwork = _AbstractNetwork
import com.google.common.graph.Network as _Network
_Network = _Network
import java.lang.String as _String
_String = _String
from builtins import object
from abc import abstractmethod, ABC
import java.util.Set as _Set
_Set = _Set
import java.util.Set as Set
import com.google.common.graph.Graph as _Graph
_Graph = _Graph
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractNetwork():
    """com.google.common.graph.AbstractNetwork"""
 
    @staticmethod
    def _wrap(java_value: _AbstractNetwork) -> 'AbstractNetwork':
        return AbstractNetwork(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractNetwork):
        """
        Dynamic initializer for AbstractNetwork.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractNetwork__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractNetwork__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def outDegree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.outDegree(N)"""
        return int._wrap(super(_AbstractNetwork, self).outDegree(node))

    @overload
    def edgeConnectingOrNull(self, nodeU: object, nodeV: object) -> object:
        """public E com.google.common.graph.AbstractNetwork.edgeConnectingOrNull(N,N)"""
        return object._wrap(super(_AbstractNetwork, self).edgeConnectingOrNull(nodeU, nodeV))

    @override
    @overload
    def asGraph(self) -> 'Graph':
        """public com.google.common.graph.Graph<N> com.google.common.graph.AbstractNetwork.asGraph()"""
        return 'Graph'._wrap(super(AbstractNetwork, self).asGraph())

    @abstractmethod
    def incidentNodes(self, edge: object):
        """public abstract com.google.common.graph.EndpointPair<N> com.google.common.graph.Network.incidentNodes(E)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractNetwork.toString()"""
        return str._wrap(super(AbstractNetwork, self).toString())

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractNetwork.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractNetwork, self).equals(obj))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def edgesConnecting(self, nodeU: object, nodeV: object) -> 'Set':
        """public java.util.Set<E> com.google.common.graph.AbstractNetwork.edgesConnecting(N,N)"""
        return 'Set'._wrap(super(_AbstractNetwork, self).edgesConnecting(nodeU, nodeV))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractNetwork.hashCode()"""
        return int._wrap(super(AbstractNetwork, self).hashCode())

    @abstractmethod
    def nodes(self, ):
        """public abstract java.util.Set<N> com.google.common.graph.Network.nodes()"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.adjacentNodes(N)"""
        pass

    @abstractmethod
    def inEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.inEdges(N)"""
        pass

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
    def inDegree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.inDegree(N)"""
        return int._wrap(super(_AbstractNetwork, self).inDegree(node))

    @overload
    def adjacentEdges(self, edge: object) -> 'Set':
        """public java.util.Set<E> com.google.common.graph.AbstractNetwork.adjacentEdges(E)"""
        return 'Set'._wrap(super(_AbstractNetwork, self).adjacentEdges(edge))

    @overload
    def __init__(self):
        """public com.google.common.graph.AbstractNetwork()"""
        val = _AbstractNetwork()
        self.__wrapper = val

    @overload
    def edgeConnecting(self, nodeU: object, nodeV: object) -> 'Optional':
        """public java.util.Optional<E> com.google.common.graph.AbstractNetwork.edgeConnecting(N,N)"""
        return 'Optional'._wrap(super(_AbstractNetwork, self).edgeConnecting(nodeU, nodeV))

    @overload
    def hasEdgeConnecting(self, endpoints: 'EndpointPair') -> bool:
        """public boolean com.google.common.graph.AbstractNetwork.hasEdgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        return bool._wrap(super(_AbstractNetwork, self).hasEdgeConnecting(endpoints))

    @overload
    def hasEdgeConnecting(self, nodeU: object, nodeV: object) -> bool:
        """public boolean com.google.common.graph.AbstractNetwork.hasEdgeConnecting(N,N)"""
        return bool._wrap(super(_AbstractNetwork, self).hasEdgeConnecting(nodeU, nodeV))

    @overload
    def degree(self, node: object) -> int:
        """public int com.google.common.graph.AbstractNetwork.degree(N)"""
        return int._wrap(super(_AbstractNetwork, self).degree(node))

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.Network.allowsSelfLoops()"""
        pass

    @overload
    def edgesConnecting(self, endpoints: 'EndpointPair') -> 'Set':
        """public java.util.Set<E> com.google.common.graph.AbstractNetwork.edgesConnecting(com.google.common.graph.EndpointPair<N>)"""
        return 'Set'._wrap(super(_AbstractNetwork, self).edgesConnecting(endpoints))

    @abstractmethod
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.Network.isDirected()"""
        pass

    @abstractmethod
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.Network.nodeOrder()"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def successors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.successors(N)"""
        pass

    @overload
    def __init__(self, ):
        """public com.google.common.graph.AbstractNetwork()"""
        val = _AbstractNetwork()
        self.__wrapper = val

    @abstractmethod
    def edgeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<E> com.google.common.graph.Network.edgeOrder()"""
        pass

    @overload
    def edgeConnectingOrNull(self, endpoints: 'EndpointPair') -> object:
        """public E com.google.common.graph.AbstractNetwork.edgeConnectingOrNull(com.google.common.graph.EndpointPair<N>)"""
        return object._wrap(super(_AbstractNetwork, self).edgeConnectingOrNull(endpoints))

    @abstractmethod
    def edges(self, ):
        """public abstract java.util.Set<E> com.google.common.graph.Network.edges()"""
        pass

    @overload
    def edgeConnecting(self, endpoints: 'EndpointPair') -> 'Optional':
        """public java.util.Optional<E> com.google.common.graph.AbstractNetwork.edgeConnecting(com.google.common.graph.EndpointPair<N>)"""
        return 'Optional'._wrap(super(_AbstractNetwork, self).edgeConnecting(endpoints))

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

    @abstractmethod
    def incidentEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.incidentEdges(N)"""
        pass

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.Network.predecessors(N)"""
        pass

    @abstractmethod
    def outEdges(self, node: object):
        """public abstract java.util.Set<E> com.google.common.graph.Network.outEdges(N)"""
        pass 
 
 
# CLASS: com.google.common.graph.EndpointPair
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import com.google.common.collect.UnmodifiableIterator as _UnmodifiableIterator
_UnmodifiableIterator = _UnmodifiableIterator
from abc import abstractmethod, ABC
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.Consumer as Consumer
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.util.Spliterator as Spliterator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import com.google.common.graph.EndpointPair as _EndpointPair
_EndpointPair = _EndpointPair
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
 
class EndpointPair():
    """com.google.common.graph.EndpointPair"""
 
    @staticmethod
    def _wrap(java_value: _EndpointPair) -> 'EndpointPair':
        return EndpointPair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EndpointPair):
        """
        Dynamic initializer for EndpointPair.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EndpointPair__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EndpointPair__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equals(self, obj: object):
        """public abstract boolean com.google.common.graph.EndpointPair.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def target(self, ):
        """public abstract N com.google.common.graph.EndpointPair.target()"""
        pass

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

    @abstractmethod
    def hashCode(self, ):
        """public abstract int com.google.common.graph.EndpointPair.hashCode()"""
        pass

    @staticmethod
    @overload
    def unordered(nodeU: object, nodeV: object) -> 'EndpointPair':
        """public static <N> com.google.common.graph.EndpointPair<N> com.google.common.graph.EndpointPair.unordered(N,N)"""
        return EndpointPair._wrap(_EndpointPair.unordered(nodeU, nodeV))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def iterator(self) -> 'pygcollect.UnmodifiableIterator':
        """public final com.google.common.collect.UnmodifiableIterator<N> com.google.common.graph.EndpointPair.iterator()"""
        return 'pygcollect.UnmodifiableIterator'._wrap(super(EndpointPair, self).iterator())

    @staticmethod
    @overload
    def ordered(source: object, target: object) -> 'EndpointPair':
        """public static <N> com.google.common.graph.EndpointPair<N> com.google.common.graph.EndpointPair.ordered(N,N)"""
        return EndpointPair._wrap(_EndpointPair.ordered(source, target))

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

    @abstractmethod
    def isOrdered(self, ):
        """public abstract boolean com.google.common.graph.EndpointPair.isOrdered()"""
        pass

    @overload
    def nodeV(self) -> object:
        """public final N com.google.common.graph.EndpointPair.nodeV()"""
        return object._wrap(super(EndpointPair, self).nodeV())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def adjacentNode(self, node: object) -> object:
        """public final N com.google.common.graph.EndpointPair.adjacentNode(N)"""
        return object._wrap(super(_EndpointPair, self).adjacentNode(node))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @abstractmethod
    def source(self, ):
        """public abstract N com.google.common.graph.EndpointPair.source()"""
        pass

    @overload
    def nodeU(self) -> object:
        """public final N com.google.common.graph.EndpointPair.nodeU()"""
        return object._wrap(super(EndpointPair, self).nodeU()) 
 
 
# CLASS: com.google.common.graph.Traverser
from builtins import str
import com.google.common.graph.Traverser as _Traverser
_Traverser = _Traverser
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Traverser():
    """com.google.common.graph.Traverser"""
 
    @staticmethod
    def _wrap(java_value: _Traverser) -> 'Traverser':
        return Traverser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Traverser):
        """
        Dynamic initializer for Traverser.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Traverser__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Traverser__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def breadthFirst(self, startNodes: 'Iterable') -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.breadthFirst(java.lang.Iterable<? extends N>)"""
        return 'Iterable'._wrap(super(_Traverser, self).breadthFirst(startNodes))

    @overload
    def depthFirstPreOrder(self, startNode: object) -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.depthFirstPreOrder(N)"""
        return 'Iterable'._wrap(super(_Traverser, self).depthFirstPreOrder(startNode))

    @staticmethod
    @overload
    def forTree(tree: 'SuccessorsFunction') -> 'Traverser':
        """public static <N> com.google.common.graph.Traverser<N> com.google.common.graph.Traverser.forTree(com.google.common.graph.SuccessorsFunction<N>)"""
        return Traverser._wrap(_Traverser.forTree(tree))

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
    def depthFirstPostOrder(self, startNodes: 'Iterable') -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.depthFirstPostOrder(java.lang.Iterable<? extends N>)"""
        return 'Iterable'._wrap(super(_Traverser, self).depthFirstPostOrder(startNodes))

    @overload
    def depthFirstPreOrder(self, startNodes: 'Iterable') -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.depthFirstPreOrder(java.lang.Iterable<? extends N>)"""
        return 'Iterable'._wrap(super(_Traverser, self).depthFirstPreOrder(startNodes))

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

    @staticmethod
    @overload
    def forGraph(graph: 'SuccessorsFunction') -> 'Traverser':
        """public static <N> com.google.common.graph.Traverser<N> com.google.common.graph.Traverser.forGraph(com.google.common.graph.SuccessorsFunction<N>)"""
        return Traverser._wrap(_Traverser.forGraph(graph))

    @overload
    def breadthFirst(self, startNode: object) -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.breadthFirst(N)"""
        return 'Iterable'._wrap(super(_Traverser, self).breadthFirst(startNode))

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
    def depthFirstPostOrder(self, startNode: object) -> 'Iterable':
        """public final java.lang.Iterable<N> com.google.common.graph.Traverser.depthFirstPostOrder(N)"""
        return 'Iterable'._wrap(super(_Traverser, self).depthFirstPostOrder(startNode))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.graph.ImmutableValueGraph$Builder
from builtins import str
from pyquantum_helper import override
import com.google.common.graph.ImmutableValueGraph as _ImmutableValueGraph_Builder
_Builder = _ImmutableValueGraph_Builder.Builder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.graph.ImmutableValueGraph as _ImmutableValueGraph
_ImmutableValueGraph = _ImmutableValueGraph
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """com.google.common.graph.ImmutableValueGraph.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addNode(self, node: object) -> 'Builder':
        """public com.google.common.graph.ImmutableValueGraph$Builder<N, V> com.google.common.graph.ImmutableValueGraph$Builder.addNode(N)"""
        return 'Builder'._wrap(super(_Builder, self).addNode(node))

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

    @overload
    def putEdgeValue(self, endpoints: 'EndpointPair', value: object) -> 'Builder':
        """public com.google.common.graph.ImmutableValueGraph$Builder<N, V> com.google.common.graph.ImmutableValueGraph$Builder.putEdgeValue(com.google.common.graph.EndpointPair<N>,V)"""
        return 'Builder'._wrap(super(_Builder, self).putEdgeValue(endpoints, value))

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
    def build(self) -> 'ImmutableValueGraph':
        """public com.google.common.graph.ImmutableValueGraph<N, V> com.google.common.graph.ImmutableValueGraph$Builder.build()"""
        return 'ImmutableValueGraph'._wrap(super(Builder, self).build())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def putEdgeValue(self, nodeU: object, nodeV: object, value: object) -> 'Builder':
        """public com.google.common.graph.ImmutableValueGraph$Builder<N, V> com.google.common.graph.ImmutableValueGraph$Builder.putEdgeValue(N,N,V)"""
        return 'Builder'._wrap(super(_Builder, self).putEdgeValue(nodeU, nodeV, value))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.graph.ImmutableGraph$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.graph.ImmutableGraph as _ImmutableGraph_Builder
_Builder = _ImmutableGraph_Builder.Builder
import java.lang.String as _String
_String = _String
import com.google.common.graph.ImmutableGraph as _ImmutableGraph
_ImmutableGraph = _ImmutableGraph
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """com.google.common.graph.ImmutableGraph.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def putEdge(self, nodeU: object, nodeV: object) -> 'Builder':
        """public com.google.common.graph.ImmutableGraph$Builder<N> com.google.common.graph.ImmutableGraph$Builder.putEdge(N,N)"""
        return 'Builder'._wrap(super(_Builder, self).putEdge(nodeU, nodeV))

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def putEdge(self, endpoints: 'EndpointPair') -> 'Builder':
        """public com.google.common.graph.ImmutableGraph$Builder<N> com.google.common.graph.ImmutableGraph$Builder.putEdge(com.google.common.graph.EndpointPair<N>)"""
        return 'Builder'._wrap(super(_Builder, self).putEdge(endpoints))

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
    def build(self) -> 'ImmutableGraph':
        """public com.google.common.graph.ImmutableGraph<N> com.google.common.graph.ImmutableGraph$Builder.build()"""
        return 'ImmutableGraph'._wrap(super(Builder, self).build())

    @overload
    def addNode(self, node: object) -> 'Builder':
        """public com.google.common.graph.ImmutableGraph$Builder<N> com.google.common.graph.ImmutableGraph$Builder.addNode(N)"""
        return 'Builder'._wrap(super(_Builder, self).addNode(node))

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
 
 
# CLASS: com.google.common.graph.MutableNetwork
import com.google.common.graph.Network as _Network
_Network = _Network
from abc import abstractmethod, ABC
import com.google.common.graph.MutableNetwork as _MutableNetwork
_MutableNetwork = _MutableNetwork
 
class MutableNetwork():
    """com.google.common.graph.MutableNetwork"""
 
    @staticmethod
    def _wrap(java_value: _MutableNetwork) -> 'MutableNetwork':
        return MutableNetwork(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableNetwork):
        """
        Dynamic initializer for MutableNetwork.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableNetwork__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableNetwork__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.google.common.graph.Graph
import com.google.common.graph.Graph as _Graph
_Graph = _Graph
from abc import abstractmethod, ABC
 
class Graph():
    """com.google.common.graph.Graph"""
 
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
 
 
# CLASS: com.google.common.graph.AbstractValueGraph
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.graph.ValueGraph as _ValueGraph
_ValueGraph = _ValueGraph
from abc import abstractmethod, ABC
import com.google.common.graph.Graph as _Graph
_Graph = _Graph
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import com.google.common.graph.AbstractValueGraph as _AbstractValueGraph
_AbstractValueGraph = _AbstractValueGraph
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractValueGraph():
    """com.google.common.graph.AbstractValueGraph"""
 
    @staticmethod
    def _wrap(java_value: _AbstractValueGraph) -> 'AbstractValueGraph':
        return AbstractValueGraph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractValueGraph):
        """
        Dynamic initializer for AbstractValueGraph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractValueGraph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractValueGraph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def asGraph(self) -> 'Graph':
        """public com.google.common.graph.Graph<N> com.google.common.graph.AbstractValueGraph.asGraph()"""
        return 'Graph'._wrap(super(AbstractValueGraph, self).asGraph())

    @abstractmethod
    def nodeOrder(self, ):
        """public abstract com.google.common.graph.ElementOrder<N> com.google.common.graph.ValueGraph.nodeOrder()"""
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
    def edgeValueOrDefault(self, endpoints: 'EndpointPair', defaultValue: object):
        """public abstract V com.google.common.graph.ValueGraph.edgeValueOrDefault(com.google.common.graph.EndpointPair<N>,V)"""
        pass

    @overload
    def __init__(self, ):
        """public com.google.common.graph.AbstractValueGraph()"""
        val = _AbstractValueGraph()
        self.__wrapper = val

    @overload
    def edgeValue(self, nodeU: object, nodeV: object) -> 'Optional':
        """public java.util.Optional<V> com.google.common.graph.AbstractValueGraph.edgeValue(N,N)"""
        return 'Optional'._wrap(super(_AbstractValueGraph, self).edgeValue(nodeU, nodeV))

    @abstractmethod
    def predecessors(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.predecessors(N)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.google.common.graph.AbstractValueGraph()"""
        val = _AbstractValueGraph()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def isDirected(self, ):
        """public abstract boolean com.google.common.graph.ValueGraph.isDirected()"""
        pass

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
    def toString(self) -> str:
        """public java.lang.String com.google.common.graph.AbstractValueGraph.toString()"""
        return str._wrap(super(AbstractValueGraph, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def edgeValueOrDefault(self, nodeU: object, nodeV: object, defaultValue: object):
        """public abstract V com.google.common.graph.ValueGraph.edgeValueOrDefault(N,N,V)"""
        pass

    @overload
    def equals(self, obj: object) -> bool:
        """public final boolean com.google.common.graph.AbstractValueGraph.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractValueGraph, self).equals(obj))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def adjacentNodes(self, node: object):
        """public abstract java.util.Set<N> com.google.common.graph.ValueGraph.adjacentNodes(N)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.common.graph.AbstractValueGraph.hashCode()"""
        return int._wrap(super(AbstractValueGraph, self).hashCode())

    @abstractmethod
    def allowsSelfLoops(self, ):
        """public abstract boolean com.google.common.graph.ValueGraph.allowsSelfLoops()"""
        pass

    @overload
    def edgeValue(self, endpoints: 'EndpointPair') -> 'Optional':
        """public java.util.Optional<V> com.google.common.graph.AbstractValueGraph.edgeValue(com.google.common.graph.EndpointPair<N>)"""
        return 'Optional'._wrap(super(_AbstractValueGraph, self).edgeValue(endpoints)) 
 
 
# CLASS: com.google.common.graph.ElementOrder$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import com.google.common.graph.ElementOrder as _ElementOrder_Type
_Type = _ElementOrder_Type.Type
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """com.google.common.graph.ElementOrder.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.google.common.graph.ElementOrder$Type[] com.google.common.graph.ElementOrder$Type.values()"""
        return List[Type]._wrap(_Type.values())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(name: str) -> 'Type':
        """public static com.google.common.graph.ElementOrder$Type com.google.common.graph.ElementOrder$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(name))