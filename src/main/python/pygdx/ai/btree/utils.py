from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_Adapter
__Adapter = __DistributionAdapters_Adapter.Adapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pygdx.ai.utils import random
except ImportError:
    random = __import_once__("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_IntegerAdapter
__IntegerAdapter = __DistributionAdapters_IntegerAdapter.IntegerAdapter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntegerAdapter(ABC):
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.IntegerAdapter"""
 
    @staticmethod
    def __wrap(java_value: __IntegerAdapter) -> 'IntegerAdapter':
        return IntegerAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntegerAdapter):
        """
        Dynamic initializer for IntegerAdapter.
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
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int.__wrap(__Adapter.parseInteger(arg0))

    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int.__wrap(__Adapter.parseLong(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$IntegerAdapter(java.lang.String)"""
        val = __IntegerAdapter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float.__wrap(__Adapter.parseDouble(arg0))

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

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float.__wrap(__Adapter.parseFloat(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$IntegerAdapter
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_Adapter
__Adapter = __DistributionAdapters_Adapter.Adapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pygdx.ai.utils import random
except ImportError:
    random = __import_once__("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_IntegerAdapter
__IntegerAdapter = __DistributionAdapters_IntegerAdapter.IntegerAdapter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntegerAdapter(ABC):
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.IntegerAdapter"""
 
    @staticmethod
    def __wrap(java_value: __IntegerAdapter) -> 'IntegerAdapter':
        return IntegerAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntegerAdapter):
        """
        Dynamic initializer for IntegerAdapter.
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
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int.__wrap(__Adapter.parseInteger(arg0))

    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int.__wrap(__Adapter.parseLong(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$IntegerAdapter(java.lang.String)"""
        val = __IntegerAdapter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float.__wrap(__Adapter.parseDouble(arg0))

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

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float.__wrap(__Adapter.parseFloat(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$IntegerAdapter 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$Subtree
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as __BehaviorTreeParser_DefaultBehaviorTreeReader_Subtree
__Subtree = __BehaviorTreeParser_DefaultBehaviorTreeReader_Subtree.DefaultBehaviorTreeReader.Subtree
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Subtree():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.DefaultBehaviorTreeReader.Subtree"""
 
    @staticmethod
    def __wrap(java_value: __Subtree) -> 'Subtree':
        return Subtree(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Subtree):
        """
        Dynamic initializer for Subtree.
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
    def rootTaskInstance(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$Subtree.rootTaskInstance()"""
        return 'btree.Task'.__wrap(super(Subtree, self).rootTaskInstance())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isRootTree(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$Subtree.isRootTree()"""
        return bool.__wrap(super(Subtree, self).isRootTree())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def init(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$Subtree.init(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(__Subtree, self).init(arg0)

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
    def inited(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$Subtree.inited()"""
        return bool.__wrap(super(Subtree, self).inited())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.ai.utils.random.Distribution as __Distribution
__Distribution = __Distribution
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.ai.utils import random
except ImportError:
    random = __import_once__("pygdx.ai.utils.random")

import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters
__DistributionAdapters = __DistributionAdapters
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DistributionAdapters():
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters"""
 
    @staticmethod
    def __wrap(java_value: __DistributionAdapters) -> 'DistributionAdapters':
        return DistributionAdapters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DistributionAdapters):
        """
        Dynamic initializer for DistributionAdapters.
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
    def toString(self, arg0: 'Distribution') -> str:
        """public java.lang.String com.badlogic.gdx.ai.btree.utils.DistributionAdapters.toString(com.badlogic.gdx.ai.utils.random.Distribution)"""
        return str.__wrap(super(__DistributionAdapters, self).toString(arg0))

    @overload
    def add(self, arg0: 'Class', arg1: 'Adapter'):
        """public final void com.badlogic.gdx.ai.btree.utils.DistributionAdapters.add(java.lang.Class<?>,com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter<?>)"""
        super(__DistributionAdapters, self).add(arg0, arg1)

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
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters()"""
        val = __DistributionAdapters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def toDistribution(self, arg0: str, arg1: 'Class') -> 'random.Distribution':
        """public <T extends com.badlogic.gdx.ai.utils.random.Distribution> T com.badlogic.gdx.ai.btree.utils.DistributionAdapters.toDistribution(java.lang.String,java.lang.Class<T>)"""
        return 'random.Distribution'.__wrap(super(__DistributionAdapters, self).toDistribution(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters()"""
        val = __DistributionAdapters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$FloatAdapter
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_Adapter
__Adapter = __DistributionAdapters_Adapter.Adapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pygdx.ai.utils import random
except ImportError:
    random = __import_once__("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_FloatAdapter
__FloatAdapter = __DistributionAdapters_FloatAdapter.FloatAdapter
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FloatAdapter(ABC):
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.FloatAdapter"""
 
    @staticmethod
    def __wrap(java_value: __FloatAdapter) -> 'FloatAdapter':
        return FloatAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatAdapter):
        """
        Dynamic initializer for FloatAdapter.
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
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int.__wrap(__Adapter.parseInteger(arg0))

    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int.__wrap(__Adapter.parseLong(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float.__wrap(__Adapter.parseDouble(arg0))

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
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$FloatAdapter(java.lang.String)"""
        val = __FloatAdapter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float.__wrap(__Adapter.parseFloat(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$StackedTask
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
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as __BehaviorTreeParser_DefaultBehaviorTreeReader_StackedTask
__StackedTask = __BehaviorTreeParser_DefaultBehaviorTreeReader_StackedTask.DefaultBehaviorTreeReader.StackedTask
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StackedTask():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.DefaultBehaviorTreeReader.StackedTask"""
 
    @staticmethod
    def __wrap(java_value: __StackedTask) -> 'StackedTask':
        return StackedTask(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StackedTask):
        """
        Dynamic initializer for StackedTask.
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
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader as __BehaviorTreeLoader
__BehaviorTreeLoader = __BehaviorTreeLoader
from pyquantum_helper import override
import com.badlogic.gdx.ai.btree.BehaviorTree as __BehaviorTree
__BehaviorTree = __BehaviorTree
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as __AsynchronousAssetLoader
__AsynchronousAssetLoader = __AsynchronousAssetLoader
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.assets.loaders.AssetLoader as __AssetLoader
__AssetLoader = __AssetLoader
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BehaviorTreeLoader():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader"""
 
    @staticmethod
    def __wrap(java_value: __BehaviorTreeLoader) -> 'BehaviorTreeLoader':
        return BehaviorTreeLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BehaviorTreeLoader):
        """
        Dynamic initializer for BehaviorTreeLoader.
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
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__loaders.AssetLoader, self).resolve(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'BehaviorTreeParameter') -> 'btree.BehaviorTree':
        """public com.badlogic.gdx.ai.btree.BehaviorTree com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter)"""
        return 'btree.BehaviorTree'.__wrap(super(__BehaviorTreeLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'BehaviorTreeParameter'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter)"""
        super(__BehaviorTreeLoader, self).loadAsync(arg0, arg1, arg2, arg3)

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
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'BehaviorTreeParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter)"""
        return 'utils.Array'.__wrap(super(__BehaviorTreeLoader, self).getDependencies(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(__loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __BehaviorTreeLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.ai.btree.BehaviorTree as __BehaviorTree
__BehaviorTree = __BehaviorTree
from builtins import type
import com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary as __PooledBehaviorTreeLibrary
__PooledBehaviorTreeLibrary = __PooledBehaviorTreeLibrary
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary as __BehaviorTreeLibrary
__BehaviorTreeLibrary = __BehaviorTreeLibrary
from builtins import int
 
class PooledBehaviorTreeLibrary():
    """com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary"""
 
    @staticmethod
    def __wrap(java_value: __PooledBehaviorTreeLibrary) -> 'PooledBehaviorTreeLibrary':
        return PooledBehaviorTreeLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PooledBehaviorTreeLibrary):
        """
        Dynamic initializer for PooledBehaviorTreeLibrary.
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
    def registerArchetypeTree(self, arg0: str, arg1: 'BehaviorTree'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.registerArchetypeTree(java.lang.String,com.badlogic.gdx.ai.btree.BehaviorTree<?>)"""
        super(__BehaviorTreeLibrary, self).registerArchetypeTree(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def clear(self, arg0: str):
        """public void com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary.clear(java.lang.String)"""
        super(__PooledBehaviorTreeLibrary, self).clear(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def hasArchetypeTree(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.hasArchetypeTree(java.lang.String)"""
        return bool.__wrap(super(__BehaviorTreeLibrary, self).hasArchetypeTree(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def createBehaviorTree(self, arg0: str, arg1: object) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary.createBehaviorTree(java.lang.String,T)"""
        return 'btree.BehaviorTree'.__wrap(super(__PooledBehaviorTreeLibrary, self).createBehaviorTree(arg0, arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary()"""
        val = __PooledBehaviorTreeLibrary()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary()"""
        val = __PooledBehaviorTreeLibrary()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def disposeBehaviorTree(self, arg0: str, arg1: 'BehaviorTree'):
        """public void com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary.disposeBehaviorTree(java.lang.String,com.badlogic.gdx.ai.btree.BehaviorTree<?>)"""
        super(__PooledBehaviorTreeLibrary, self).disposeBehaviorTree(arg0, arg1)

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
    def createBehaviorTree(self, arg0: str) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.createBehaviorTree(java.lang.String)"""
        return 'btree.BehaviorTree'.__wrap(super(__BehaviorTreeLibrary, self).createBehaviorTree(arg0))

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
    def createRootTask(self, arg0: str) -> 'btree.Task':
        """public <T> com.badlogic.gdx.ai.btree.Task<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.createRootTask(java.lang.String)"""
        return 'btree.Task'.__wrap(super(__BehaviorTreeLibrary, self).createRootTask(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary.clear()"""
        super(PooledBehaviorTreeLibrary, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.ai.btree.BehaviorTree as __BehaviorTree
__BehaviorTree = __BehaviorTree
from builtins import type
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary as __BehaviorTreeLibrary
__BehaviorTreeLibrary = __BehaviorTreeLibrary
from builtins import int
 
class BehaviorTreeLibrary():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary"""
 
    @staticmethod
    def __wrap(java_value: __BehaviorTreeLibrary) -> 'BehaviorTreeLibrary':
        return BehaviorTreeLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BehaviorTreeLibrary):
        """
        Dynamic initializer for BehaviorTreeLibrary.
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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary(int)"""
        val = __BehaviorTreeLibrary(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary()"""
        val = __BehaviorTreeLibrary()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def createBehaviorTree(self, arg0: str, arg1: object) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.createBehaviorTree(java.lang.String,T)"""
        return 'btree.BehaviorTree'.__wrap(super(__BehaviorTreeLibrary, self).createBehaviorTree(arg0, arg1))

    @overload
    def hasArchetypeTree(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.hasArchetypeTree(java.lang.String)"""
        return bool.__wrap(super(__BehaviorTreeLibrary, self).hasArchetypeTree(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary()"""
        val = __BehaviorTreeLibrary()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def createBehaviorTree(self, arg0: str) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.createBehaviorTree(java.lang.String)"""
        return 'btree.BehaviorTree'.__wrap(super(__BehaviorTreeLibrary, self).createBehaviorTree(arg0))

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __BehaviorTreeLibrary(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def disposeBehaviorTree(self, arg0: str, arg1: 'BehaviorTree'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.disposeBehaviorTree(java.lang.String,com.badlogic.gdx.ai.btree.BehaviorTree<?>)"""
        super(__BehaviorTreeLibrary, self).disposeBehaviorTree(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def createRootTask(self, arg0: str) -> 'btree.Task':
        """public <T> com.badlogic.gdx.ai.btree.Task<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.createRootTask(java.lang.String)"""
        return 'btree.Task'.__wrap(super(__BehaviorTreeLibrary, self).createRootTask(arg0))

    @overload
    def __init__(self, arg0: 'FileHandleResolver', arg1: int):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary(com.badlogic.gdx.assets.loaders.FileHandleResolver,int)"""
        val = __BehaviorTreeLibrary(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def registerArchetypeTree(self, arg0: str, arg1: 'BehaviorTree'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.registerArchetypeTree(java.lang.String,com.badlogic.gdx.ai.btree.BehaviorTree<?>)"""
        super(__BehaviorTreeLibrary, self).registerArchetypeTree(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.ai.btree.BehaviorTree as __BehaviorTree
__BehaviorTree = __BehaviorTree
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager as __BehaviorTreeLibraryManager
__BehaviorTreeLibraryManager = __BehaviorTreeLibraryManager
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.btree.Task as __Task
__Task = __Task
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary as __BehaviorTreeLibrary
__BehaviorTreeLibrary = __BehaviorTreeLibrary
from builtins import int
 
class BehaviorTreeLibraryManager():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager"""
 
    @staticmethod
    def __wrap(java_value: __BehaviorTreeLibraryManager) -> 'BehaviorTreeLibraryManager':
        return BehaviorTreeLibraryManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BehaviorTreeLibraryManager):
        """
        Dynamic initializer for BehaviorTreeLibraryManager.
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
    def createBehaviorTree(self, arg0: str) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.createBehaviorTree(java.lang.String)"""
        return 'btree.BehaviorTree'.__wrap(super(__BehaviorTreeLibraryManager, self).createBehaviorTree(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def createRootTask(self, arg0: str) -> 'btree.Task':
        """public <T> com.badlogic.gdx.ai.btree.Task<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.createRootTask(java.lang.String)"""
        return 'btree.Task'.__wrap(super(__BehaviorTreeLibraryManager, self).createRootTask(arg0))

    @overload
    def createBehaviorTree(self, arg0: str, arg1: object) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.createBehaviorTree(java.lang.String,T)"""
        return 'btree.BehaviorTree'.__wrap(super(__BehaviorTreeLibraryManager, self).createBehaviorTree(arg0, arg1))

    @overload
    def disposeBehaviorTree(self, arg0: str, arg1: 'BehaviorTree'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.disposeBehaviorTree(java.lang.String,com.badlogic.gdx.ai.btree.BehaviorTree<?>)"""
        super(__BehaviorTreeLibraryManager, self).disposeBehaviorTree(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getInstance() -> 'BehaviorTreeLibraryManager':
        """public static com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.getInstance()"""
        return BehaviorTreeLibraryManager.__wrap(__BehaviorTreeLibraryManager.getInstance())

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
    def getLibrary(self) -> 'BehaviorTreeLibrary':
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.getLibrary()"""
        return 'BehaviorTreeLibrary'.__wrap(super(BehaviorTreeLibraryManager, self).getLibrary())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setLibrary(self, arg0: 'BehaviorTreeLibrary'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.setLibrary(com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary)"""
        super(__BehaviorTreeLibraryManager, self).setLibrary(arg0) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader as __BehaviorTreeReader
__BehaviorTreeReader = __BehaviorTreeReader
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class BehaviorTreeReader(ABC):
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader"""
 
    @staticmethod
    def __wrap(java_value: __BehaviorTreeReader) -> 'BehaviorTreeReader':
        return BehaviorTreeReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BehaviorTreeReader):
        """
        Dynamic initializer for BehaviorTreeReader.
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
    def parse(self, arg0: 'Reader'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.io.Reader)"""
        super(__BehaviorTreeReader, self).parse(arg0)

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
    def parse(self, arg0: 'char', arg1: int, arg2: int):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(char[],int,int)"""
        super(__BehaviorTreeReader, self).parse(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def parse(self, arg0: str):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.lang.String)"""
        super(__BehaviorTreeReader, self).parse(arg0)

    @overload
    def parse(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(com.badlogic.gdx.files.FileHandle)"""
        super(__BehaviorTreeReader, self).parse(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader()"""
        val = __BehaviorTreeReader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader(boolean)"""
        val = __BehaviorTreeReader(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader()"""
        val = __BehaviorTreeReader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def parse(self, arg0: 'InputStream'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.io.InputStream)"""
        super(__BehaviorTreeReader, self).parse(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DoubleAdapter
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_Adapter
__Adapter = __DistributionAdapters_Adapter.Adapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pygdx.ai.utils import random
except ImportError:
    random = __import_once__("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_DoubleAdapter
__DoubleAdapter = __DistributionAdapters_DoubleAdapter.DoubleAdapter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DoubleAdapter(ABC):
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.DoubleAdapter"""
 
    @staticmethod
    def __wrap(java_value: __DoubleAdapter) -> 'DoubleAdapter':
        return DoubleAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleAdapter):
        """
        Dynamic initializer for DoubleAdapter.
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
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int.__wrap(__Adapter.parseInteger(arg0))

    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int.__wrap(__Adapter.parseLong(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float.__wrap(__Adapter.parseDouble(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DoubleAdapter(java.lang.String)"""
        val = __DoubleAdapter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float.__wrap(__Adapter.parseFloat(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as __BehaviorTreeParser_DefaultBehaviorTreeReader
__DefaultBehaviorTreeReader = __BehaviorTreeParser_DefaultBehaviorTreeReader.DefaultBehaviorTreeReader
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as __BehaviorTreeParser
__BehaviorTreeParser = __BehaviorTreeParser
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader as __BehaviorTreeReader
__BehaviorTreeReader = __BehaviorTreeReader
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class DefaultBehaviorTreeReader():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.DefaultBehaviorTreeReader"""
 
    @staticmethod
    def __wrap(java_value: __DefaultBehaviorTreeReader) -> 'DefaultBehaviorTreeReader':
        return DefaultBehaviorTreeReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultBehaviorTreeReader):
        """
        Dynamic initializer for DefaultBehaviorTreeReader.
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
    def setParser(self, arg0: 'BehaviorTreeParser'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader.setParser(com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser<E>)"""
        super(__DefaultBehaviorTreeReader, self).setParser(arg0)

    @override
    @overload
    def parse(self, arg0: 'Reader'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.io.Reader)"""
        super(__BehaviorTreeReader, self).parse(arg0)

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
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader(boolean)"""
        val = __DefaultBehaviorTreeReader(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def parse(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(com.badlogic.gdx.files.FileHandle)"""
        super(__BehaviorTreeReader, self).parse(arg0)

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
    def parse(self, arg0: 'char', arg1: int, arg2: int):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader.parse(char[],int,int)"""
        super(__DefaultBehaviorTreeReader, self).parse(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader()"""
        val = __DefaultBehaviorTreeReader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def parse(self, arg0: 'InputStream'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.io.InputStream)"""
        super(__BehaviorTreeReader, self).parse(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getParser(self) -> 'BehaviorTreeParser':
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader.getParser()"""
        return 'BehaviorTreeParser'.__wrap(super(DefaultBehaviorTreeReader, self).getParser())

    @override
    @overload
    def parse(self, arg0: str):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.lang.String)"""
        super(__BehaviorTreeReader, self).parse(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader()"""
        val = __DefaultBehaviorTreeReader()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter
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
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader as __BehaviorTreeLoader_BehaviorTreeParameter
__BehaviorTreeParameter = __BehaviorTreeLoader_BehaviorTreeParameter.BehaviorTreeParameter
from builtins import int
 
class BehaviorTreeParameter():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader.BehaviorTreeParameter"""
 
    @staticmethod
    def __wrap(java_value: __BehaviorTreeParameter) -> 'BehaviorTreeParameter':
        return BehaviorTreeParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BehaviorTreeParameter):
        """
        Dynamic initializer for BehaviorTreeParameter.
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
    def __init__(self, arg0: object):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter(java.lang.Object)"""
        val = __BehaviorTreeParameter(arg0)
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: object, arg1: 'BehaviorTreeParser'):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter(java.lang.Object,com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser)"""
        val = __BehaviorTreeParameter(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter()"""
        val = __BehaviorTreeParameter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter()"""
        val = __BehaviorTreeParameter()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_DistributionFormatException
__DistributionFormatException = __DistributionAdapters_DistributionFormatException.DistributionFormatException
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DistributionFormatException():
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.DistributionFormatException"""
 
    @staticmethod
    def __wrap(java_value: __DistributionFormatException) -> 'DistributionFormatException':
        return DistributionFormatException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DistributionFormatException):
        """
        Dynamic initializer for DistributionFormatException.
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
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException(java.lang.String,java.lang.Throwable)"""
        val = __DistributionFormatException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException()"""
        val = __DistributionFormatException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException(java.lang.Throwable)"""
        val = __DistributionFormatException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException()"""
        val = __DistributionFormatException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException(java.lang.String)"""
        val = __DistributionFormatException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import com.badlogic.gdx.ai.btree.BehaviorTree as __BehaviorTree
__BehaviorTree = __BehaviorTree
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as __BehaviorTreeParser
__BehaviorTreeParser = __BehaviorTreeParser
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
try:
    from pygdx.ai import btree
except ImportError:
    btree = __import_once__("pygdx.ai.btree")

import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BehaviorTreeParser():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser"""
 
    @staticmethod
    def __wrap(java_value: __BehaviorTreeParser) -> 'BehaviorTreeParser':
        return BehaviorTreeParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BehaviorTreeParser):
        """
        Dynamic initializer for BehaviorTreeParser.
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
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser()"""
        val = __BehaviorTreeParser()
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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser()"""
        val = __BehaviorTreeParser()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'DistributionAdapters'):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser(com.badlogic.gdx.ai.btree.utils.DistributionAdapters)"""
        val = __BehaviorTreeParser(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def parse(self, arg0: str, arg1: object) -> 'btree.BehaviorTree':
        """public com.badlogic.gdx.ai.btree.BehaviorTree<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.parse(java.lang.String,E)"""
        return 'btree.BehaviorTree'.__wrap(super(__BehaviorTreeParser, self).parse(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser(int)"""
        val = __BehaviorTreeParser(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'DistributionAdapters', arg1: int):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser(com.badlogic.gdx.ai.btree.utils.DistributionAdapters,int)"""
        val = __BehaviorTreeParser(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def parse(self, arg0: 'FileHandle', arg1: object) -> 'btree.BehaviorTree':
        """public com.badlogic.gdx.ai.btree.BehaviorTree<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.parse(com.badlogic.gdx.files.FileHandle,E)"""
        return 'btree.BehaviorTree'.__wrap(super(__BehaviorTreeParser, self).parse(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def parse(self, arg0: 'InputStream', arg1: object) -> 'btree.BehaviorTree':
        """public com.badlogic.gdx.ai.btree.BehaviorTree<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.parse(java.io.InputStream,E)"""
        return 'btree.BehaviorTree'.__wrap(super(__BehaviorTreeParser, self).parse(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'DistributionAdapters', arg1: int, arg2: 'DefaultBehaviorTreeReader'):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser(com.badlogic.gdx.ai.btree.utils.DistributionAdapters,int,com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader<E>)"""
        val = __BehaviorTreeParser(arg0, __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def parse(self, arg0: 'Reader', arg1: object) -> 'btree.BehaviorTree':
        """public com.badlogic.gdx.ai.btree.BehaviorTree<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.parse(java.io.Reader,E)"""
        return 'btree.BehaviorTree'.__wrap(super(__BehaviorTreeParser, self).parse(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_Adapter
__Adapter = __DistributionAdapters_Adapter.Adapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pygdx.ai.utils import random
except ImportError:
    random = __import_once__("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Adapter(ABC):
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.Adapter"""
 
    @staticmethod
    def __wrap(java_value: __Adapter) -> 'Adapter':
        return Adapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Adapter):
        """
        Dynamic initializer for Adapter.
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
    def __init__(self, arg0: str, arg1: 'Class'):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter(java.lang.String,java.lang.Class<?>)"""
        val = __Adapter(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int.__wrap(__Adapter.parseInteger(arg0))

    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int.__wrap(__Adapter.parseLong(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float.__wrap(__Adapter.parseDouble(arg0))

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

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float.__wrap(__Adapter.parseFloat(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$LongAdapter
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_Adapter
__Adapter = __DistributionAdapters_Adapter.Adapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as __DistributionAdapters_LongAdapter
__LongAdapter = __DistributionAdapters_LongAdapter.LongAdapter
try:
    from pygdx.ai.utils import random
except ImportError:
    random = __import_once__("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LongAdapter(ABC):
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.LongAdapter"""
 
    @staticmethod
    def __wrap(java_value: __LongAdapter) -> 'LongAdapter':
        return LongAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongAdapter):
        """
        Dynamic initializer for LongAdapter.
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
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int.__wrap(__Adapter.parseInteger(arg0))

    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int.__wrap(__Adapter.parseLong(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$LongAdapter(java.lang.String)"""
        val = __LongAdapter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float.__wrap(__Adapter.parseDouble(arg0))

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

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float.__wrap(__Adapter.parseFloat(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))