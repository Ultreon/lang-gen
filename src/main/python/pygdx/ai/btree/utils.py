from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as _BehaviorTreeParser_DefaultBehaviorTreeReader_StackedTask
_StackedTask = _BehaviorTreeParser_DefaultBehaviorTreeReader_StackedTask.DefaultBehaviorTreeReader.StackedTask
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StackedTask():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.DefaultBehaviorTreeReader.StackedTask"""
 
    @staticmethod
    def _wrap(java_value: _StackedTask) -> 'StackedTask':
        return StackedTask(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StackedTask):
        """
        Dynamic initializer for StackedTask.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StackedTask__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StackedTask__wrapper":
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

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$StackedTask
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as _BehaviorTreeParser_DefaultBehaviorTreeReader_StackedTask
_StackedTask = _BehaviorTreeParser_DefaultBehaviorTreeReader_StackedTask.DefaultBehaviorTreeReader.StackedTask
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StackedTask():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.DefaultBehaviorTreeReader.StackedTask"""
 
    @staticmethod
    def _wrap(java_value: _StackedTask) -> 'StackedTask':
        return StackedTask(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StackedTask):
        """
        Dynamic initializer for StackedTask.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StackedTask__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StackedTask__wrapper":
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

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$StackedTask 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$FloatAdapter
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pygdx.ai.utils import random
except ImportError:
    random = _import_once("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters_FloatAdapter
_FloatAdapter = _DistributionAdapters_FloatAdapter.FloatAdapter
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters_Adapter
_Adapter = _DistributionAdapters_Adapter.Adapter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatAdapter():
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.FloatAdapter"""
 
    @staticmethod
    def _wrap(java_value: _FloatAdapter) -> 'FloatAdapter':
        return FloatAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatAdapter):
        """
        Dynamic initializer for FloatAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$FloatAdapter(java.lang.String)"""
        val = _FloatAdapter(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int._wrap(_Adapter.parseLong(arg0))

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

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float._wrap(_Adapter.parseFloat(arg0))

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
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float._wrap(_Adapter.parseDouble(arg0))

    @staticmethod
    @overload
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int._wrap(_Adapter.parseInteger(arg0))

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.BehaviorTree as _BehaviorTree
_BehaviorTree = _BehaviorTree
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary as _BehaviorTreeLibrary
_BehaviorTreeLibrary = _BehaviorTreeLibrary
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager as _BehaviorTreeLibraryManager
_BehaviorTreeLibraryManager = _BehaviorTreeLibraryManager
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BehaviorTreeLibraryManager():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager"""
 
    @staticmethod
    def _wrap(java_value: _BehaviorTreeLibraryManager) -> 'BehaviorTreeLibraryManager':
        return BehaviorTreeLibraryManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BehaviorTreeLibraryManager):
        """
        Dynamic initializer for BehaviorTreeLibraryManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BehaviorTreeLibraryManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BehaviorTreeLibraryManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getInstance() -> 'BehaviorTreeLibraryManager':
        """public static com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.getInstance()"""
        return BehaviorTreeLibraryManager._wrap(_BehaviorTreeLibraryManager.getInstance())

    @overload
    def getLibrary(self) -> 'BehaviorTreeLibrary':
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.getLibrary()"""
        return 'BehaviorTreeLibrary'._wrap(super(BehaviorTreeLibraryManager, self).getLibrary())

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
    def createBehaviorTree(self, arg0: str, arg1: object) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.createBehaviorTree(java.lang.String,T)"""
        return 'btree.BehaviorTree'._wrap(super(_BehaviorTreeLibraryManager, self).createBehaviorTree(arg0, arg1))

    @overload
    def createBehaviorTree(self, arg0: str) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.createBehaviorTree(java.lang.String)"""
        return 'btree.BehaviorTree'._wrap(super(_BehaviorTreeLibraryManager, self).createBehaviorTree(arg0))

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
    def setLibrary(self, arg0: 'BehaviorTreeLibrary'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.setLibrary(com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary)"""
        super(_BehaviorTreeLibraryManager, self).setLibrary(arg0)

    @overload
    def disposeBehaviorTree(self, arg0: str, arg1: 'BehaviorTree'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.disposeBehaviorTree(java.lang.String,com.badlogic.gdx.ai.btree.BehaviorTree<?>)"""
        super(_BehaviorTreeLibraryManager, self).disposeBehaviorTree(arg0, arg1)

    @overload
    def createRootTask(self, arg0: str) -> 'btree.Task':
        """public <T> com.badlogic.gdx.ai.btree.Task<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibraryManager.createRootTask(java.lang.String)"""
        return 'btree.Task'._wrap(super(_BehaviorTreeLibraryManager, self).createRootTask(arg0))

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
try:
    from pygdx.ai.utils import random
except ImportError:
    random = _import_once("pygdx.ai.utils.random")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters
_DistributionAdapters = _DistributionAdapters
import com.badlogic.gdx.ai.utils.random.Distribution as _Distribution
_Distribution = _Distribution
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DistributionAdapters():
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters"""
 
    @staticmethod
    def _wrap(java_value: _DistributionAdapters) -> 'DistributionAdapters':
        return DistributionAdapters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DistributionAdapters):
        """
        Dynamic initializer for DistributionAdapters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DistributionAdapters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DistributionAdapters__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters()"""
        val = _DistributionAdapters()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters()"""
        val = _DistributionAdapters()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def toString(self, arg0: 'Distribution') -> str:
        """public java.lang.String com.badlogic.gdx.ai.btree.utils.DistributionAdapters.toString(com.badlogic.gdx.ai.utils.random.Distribution)"""
        return str._wrap(super(_DistributionAdapters, self).toString(arg0))

    @overload
    def add(self, arg0: 'Class', arg1: 'Adapter'):
        """public final void com.badlogic.gdx.ai.btree.utils.DistributionAdapters.add(java.lang.Class<?>,com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter<?>)"""
        super(_DistributionAdapters, self).add(arg0, arg1)

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
    def toDistribution(self, arg0: str, arg1: 'Class') -> 'random.Distribution':
        """public <T extends com.badlogic.gdx.ai.utils.random.Distribution> T com.badlogic.gdx.ai.btree.utils.DistributionAdapters.toDistribution(java.lang.String,java.lang.Class<T>)"""
        return 'random.Distribution'._wrap(super(_DistributionAdapters, self).toDistribution(arg0, arg1))

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.BehaviorTree as _BehaviorTree
_BehaviorTree = _BehaviorTree
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary as _BehaviorTreeLibrary
_BehaviorTreeLibrary = _BehaviorTreeLibrary
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary as _PooledBehaviorTreeLibrary
_PooledBehaviorTreeLibrary = _PooledBehaviorTreeLibrary
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PooledBehaviorTreeLibrary():
    """com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary"""
 
    @staticmethod
    def _wrap(java_value: _PooledBehaviorTreeLibrary) -> 'PooledBehaviorTreeLibrary':
        return PooledBehaviorTreeLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PooledBehaviorTreeLibrary):
        """
        Dynamic initializer for PooledBehaviorTreeLibrary.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PooledBehaviorTreeLibrary__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PooledBehaviorTreeLibrary__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def registerArchetypeTree(self, arg0: str, arg1: 'BehaviorTree'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.registerArchetypeTree(java.lang.String,com.badlogic.gdx.ai.btree.BehaviorTree<?>)"""
        super(_BehaviorTreeLibrary, self).registerArchetypeTree(arg0, arg1)

    @overload
    def createBehaviorTree(self, arg0: str, arg1: object) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary.createBehaviorTree(java.lang.String,T)"""
        return 'btree.BehaviorTree'._wrap(super(_PooledBehaviorTreeLibrary, self).createBehaviorTree(arg0, arg1))

    @overload
    def createBehaviorTree(self, arg0: str) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.createBehaviorTree(java.lang.String)"""
        return 'btree.BehaviorTree'._wrap(super(_BehaviorTreeLibrary, self).createBehaviorTree(arg0))

    @overload
    def clear(self, arg0: str):
        """public void com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary.clear(java.lang.String)"""
        super(_PooledBehaviorTreeLibrary, self).clear(arg0)

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
    def createRootTask(self, arg0: str) -> 'btree.Task':
        """public <T> com.badlogic.gdx.ai.btree.Task<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.createRootTask(java.lang.String)"""
        return 'btree.Task'._wrap(super(_BehaviorTreeLibrary, self).createRootTask(arg0))

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
    def disposeBehaviorTree(self, arg0: str, arg1: 'BehaviorTree'):
        """public void com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary.disposeBehaviorTree(java.lang.String,com.badlogic.gdx.ai.btree.BehaviorTree<?>)"""
        super(_PooledBehaviorTreeLibrary, self).disposeBehaviorTree(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary()"""
        val = _PooledBehaviorTreeLibrary()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary()"""
        val = _PooledBehaviorTreeLibrary()
        self.__wrapper = val

    @overload
    def clear(self):
        """public void com.badlogic.gdx.ai.btree.utils.PooledBehaviorTreeLibrary.clear()"""
        super(PooledBehaviorTreeLibrary, self).clear()

    @overload
    def hasArchetypeTree(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.hasArchetypeTree(java.lang.String)"""
        return bool._wrap(super(_BehaviorTreeLibrary, self).hasArchetypeTree(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader as _BehaviorTreeReader
_BehaviorTreeReader = _BehaviorTreeReader
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.InputStream as InputStream
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BehaviorTreeReader():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader"""
 
    @staticmethod
    def _wrap(java_value: _BehaviorTreeReader) -> 'BehaviorTreeReader':
        return BehaviorTreeReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BehaviorTreeReader):
        """
        Dynamic initializer for BehaviorTreeReader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BehaviorTreeReader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BehaviorTreeReader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def parse(self, arg0: 'Reader'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.io.Reader)"""
        super(_BehaviorTreeReader, self).parse(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader()"""
        val = _BehaviorTreeReader()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader()"""
        val = _BehaviorTreeReader()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def parse(self, arg0: 'InputStream'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.io.InputStream)"""
        super(_BehaviorTreeReader, self).parse(arg0)

    @overload
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader(boolean)"""
        val = _BehaviorTreeReader(_boolean.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def parse(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(com.badlogic.gdx.files.FileHandle)"""
        super(_BehaviorTreeReader, self).parse(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def parse(self, arg0: str):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.lang.String)"""
        super(_BehaviorTreeReader, self).parse(arg0)

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
    def parse(self, arg0: 'char', arg1: int, arg2: int):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(char[],int,int)"""
        super(_BehaviorTreeReader, self).parse(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as _BehaviorTreeParser
_BehaviorTreeParser = _BehaviorTreeParser
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as _BehaviorTreeParser_DefaultBehaviorTreeReader
_DefaultBehaviorTreeReader = _BehaviorTreeParser_DefaultBehaviorTreeReader.DefaultBehaviorTreeReader
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader as _BehaviorTreeReader
_BehaviorTreeReader = _BehaviorTreeReader
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.InputStream as InputStream
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultBehaviorTreeReader():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.DefaultBehaviorTreeReader"""
 
    @staticmethod
    def _wrap(java_value: _DefaultBehaviorTreeReader) -> 'DefaultBehaviorTreeReader':
        return DefaultBehaviorTreeReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultBehaviorTreeReader):
        """
        Dynamic initializer for DefaultBehaviorTreeReader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultBehaviorTreeReader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultBehaviorTreeReader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def parse(self, arg0: 'char', arg1: int, arg2: int):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader.parse(char[],int,int)"""
        super(_DefaultBehaviorTreeReader, self).parse(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def setParser(self, arg0: 'BehaviorTreeParser'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader.setParser(com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser<E>)"""
        super(_DefaultBehaviorTreeReader, self).setParser(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader()"""
        val = _DefaultBehaviorTreeReader()
        self.__wrapper = val

    @override
    @overload
    def parse(self, arg0: 'Reader'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.io.Reader)"""
        super(_BehaviorTreeReader, self).parse(arg0)

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
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader(boolean)"""
        val = _DefaultBehaviorTreeReader(_boolean.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def parse(self, arg0: 'InputStream'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.io.InputStream)"""
        super(_BehaviorTreeReader, self).parse(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def parse(self, arg0: str):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(java.lang.String)"""
        super(_BehaviorTreeReader, self).parse(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader()"""
        val = _DefaultBehaviorTreeReader()
        self.__wrapper = val

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
    def getParser(self) -> 'BehaviorTreeParser':
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader.getParser()"""
        return 'BehaviorTreeParser'._wrap(super(DefaultBehaviorTreeReader, self).getParser())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def parse(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeReader.parse(com.badlogic.gdx.files.FileHandle)"""
        super(_BehaviorTreeReader, self).parse(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DoubleAdapter
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pygdx.ai.utils import random
except ImportError:
    random = _import_once("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters_Adapter
_Adapter = _DistributionAdapters_Adapter.Adapter
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters_DoubleAdapter
_DoubleAdapter = _DistributionAdapters_DoubleAdapter.DoubleAdapter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DoubleAdapter():
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.DoubleAdapter"""
 
    @staticmethod
    def _wrap(java_value: _DoubleAdapter) -> 'DoubleAdapter':
        return DoubleAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleAdapter):
        """
        Dynamic initializer for DoubleAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int._wrap(_Adapter.parseLong(arg0))

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

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float._wrap(_Adapter.parseFloat(arg0))

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
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float._wrap(_Adapter.parseDouble(arg0))

    @staticmethod
    @overload
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int._wrap(_Adapter.parseInteger(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DoubleAdapter(java.lang.String)"""
        val = _DoubleAdapter(arg0)
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
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pygdx.ai.utils import random
except ImportError:
    random = _import_once("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters_Adapter
_Adapter = _DistributionAdapters_Adapter.Adapter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Adapter():
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.Adapter"""
 
    @staticmethod
    def _wrap(java_value: _Adapter) -> 'Adapter':
        return Adapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Adapter):
        """
        Dynamic initializer for Adapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Adapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Adapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str, arg1: 'Class'):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter(java.lang.String,java.lang.Class<?>)"""
        val = _Adapter(arg0, arg1)
        self.__wrapper = val

    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int._wrap(_Adapter.parseLong(arg0))

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

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float._wrap(_Adapter.parseFloat(arg0))

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
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float._wrap(_Adapter.parseDouble(arg0))

    @staticmethod
    @overload
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int._wrap(_Adapter.parseInteger(arg0))

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as _BehaviorTreeParser
_BehaviorTreeParser = _BehaviorTreeParser
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.BehaviorTree as _BehaviorTree
_BehaviorTree = _BehaviorTree
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import java.io.Reader as Reader
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

import java.io.InputStream as InputStream
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BehaviorTreeParser():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser"""
 
    @staticmethod
    def _wrap(java_value: _BehaviorTreeParser) -> 'BehaviorTreeParser':
        return BehaviorTreeParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BehaviorTreeParser):
        """
        Dynamic initializer for BehaviorTreeParser.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BehaviorTreeParser__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BehaviorTreeParser__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser()"""
        val = _BehaviorTreeParser()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'DistributionAdapters'):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser(com.badlogic.gdx.ai.btree.utils.DistributionAdapters)"""
        val = _BehaviorTreeParser(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser()"""
        val = _BehaviorTreeParser()
        self.__wrapper = val

    @overload
    def parse(self, arg0: 'InputStream', arg1: object) -> 'btree.BehaviorTree':
        """public com.badlogic.gdx.ai.btree.BehaviorTree<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.parse(java.io.InputStream,E)"""
        return 'btree.BehaviorTree'._wrap(super(_BehaviorTreeParser, self).parse(arg0, arg1))

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser(int)"""
        val = _BehaviorTreeParser(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'DistributionAdapters', arg1: int, arg2: 'DefaultBehaviorTreeReader'):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser(com.badlogic.gdx.ai.btree.utils.DistributionAdapters,int,com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader<E>)"""
        val = _BehaviorTreeParser(arg0, _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def parse(self, arg0: 'FileHandle', arg1: object) -> 'btree.BehaviorTree':
        """public com.badlogic.gdx.ai.btree.BehaviorTree<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.parse(com.badlogic.gdx.files.FileHandle,E)"""
        return 'btree.BehaviorTree'._wrap(super(_BehaviorTreeParser, self).parse(arg0, arg1))

    @overload
    def parse(self, arg0: 'Reader', arg1: object) -> 'btree.BehaviorTree':
        """public com.badlogic.gdx.ai.btree.BehaviorTree<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.parse(java.io.Reader,E)"""
        return 'btree.BehaviorTree'._wrap(super(_BehaviorTreeParser, self).parse(arg0, arg1))

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
    def __init__(self, arg0: 'DistributionAdapters', arg1: int):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser(com.badlogic.gdx.ai.btree.utils.DistributionAdapters,int)"""
        val = _BehaviorTreeParser(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def parse(self, arg0: str, arg1: object) -> 'btree.BehaviorTree':
        """public com.badlogic.gdx.ai.btree.BehaviorTree<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.parse(java.lang.String,E)"""
        return 'btree.BehaviorTree'._wrap(super(_BehaviorTreeParser, self).parse(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.BehaviorTree as _BehaviorTree
_BehaviorTree = _BehaviorTree
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary as _BehaviorTreeLibrary
_BehaviorTreeLibrary = _BehaviorTreeLibrary
import java.lang.String as _String
_String = _String
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import java.lang.String as _string
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BehaviorTreeLibrary():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary"""
 
    @staticmethod
    def _wrap(java_value: _BehaviorTreeLibrary) -> 'BehaviorTreeLibrary':
        return BehaviorTreeLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BehaviorTreeLibrary):
        """
        Dynamic initializer for BehaviorTreeLibrary.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BehaviorTreeLibrary__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BehaviorTreeLibrary__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _BehaviorTreeLibrary(arg0)
        self.__wrapper = val

    @overload
    def createBehaviorTree(self, arg0: str) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.createBehaviorTree(java.lang.String)"""
        return 'btree.BehaviorTree'._wrap(super(_BehaviorTreeLibrary, self).createBehaviorTree(arg0))

    @overload
    def createBehaviorTree(self, arg0: str, arg1: object) -> 'btree.BehaviorTree':
        """public <T> com.badlogic.gdx.ai.btree.BehaviorTree<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.createBehaviorTree(java.lang.String,T)"""
        return 'btree.BehaviorTree'._wrap(super(_BehaviorTreeLibrary, self).createBehaviorTree(arg0, arg1))

    @overload
    def registerArchetypeTree(self, arg0: str, arg1: 'BehaviorTree'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.registerArchetypeTree(java.lang.String,com.badlogic.gdx.ai.btree.BehaviorTree<?>)"""
        super(_BehaviorTreeLibrary, self).registerArchetypeTree(arg0, arg1)

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
    def createRootTask(self, arg0: str) -> 'btree.Task':
        """public <T> com.badlogic.gdx.ai.btree.Task<T> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.createRootTask(java.lang.String)"""
        return 'btree.Task'._wrap(super(_BehaviorTreeLibrary, self).createRootTask(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary()"""
        val = _BehaviorTreeLibrary()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def disposeBehaviorTree(self, arg0: str, arg1: 'BehaviorTree'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.disposeBehaviorTree(java.lang.String,com.badlogic.gdx.ai.btree.BehaviorTree<?>)"""
        super(_BehaviorTreeLibrary, self).disposeBehaviorTree(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'FileHandleResolver', arg1: int):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary(com.badlogic.gdx.assets.loaders.FileHandleResolver,int)"""
        val = _BehaviorTreeLibrary(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary()"""
        val = _BehaviorTreeLibrary()
        self.__wrapper = val

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
    def hasArchetypeTree(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary.hasArchetypeTree(java.lang.String)"""
        return bool._wrap(super(_BehaviorTreeLibrary, self).hasArchetypeTree(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLibrary(int)"""
        val = _BehaviorTreeLibrary(_int.valueOf(arg0))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters_DistributionFormatException
_DistributionFormatException = _DistributionAdapters_DistributionFormatException.DistributionFormatException
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DistributionFormatException():
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.DistributionFormatException"""
 
    @staticmethod
    def _wrap(java_value: _DistributionFormatException) -> 'DistributionFormatException':
        return DistributionFormatException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DistributionFormatException):
        """
        Dynamic initializer for DistributionFormatException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DistributionFormatException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DistributionFormatException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException(java.lang.String,java.lang.Throwable)"""
        val = _DistributionFormatException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException(java.lang.String)"""
        val = _DistributionFormatException(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException()"""
        val = _DistributionFormatException()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException(java.lang.Throwable)"""
        val = _DistributionFormatException(arg0)
        self.__wrapper = val

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$DistributionFormatException()"""
        val = _DistributionFormatException()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.BehaviorTree as _BehaviorTree
_BehaviorTree = _BehaviorTree
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader as _BehaviorTreeLoader
_BehaviorTreeLoader = _BehaviorTreeLoader
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BehaviorTreeLoader():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader"""
 
    @staticmethod
    def _wrap(java_value: _BehaviorTreeLoader) -> 'BehaviorTreeLoader':
        return BehaviorTreeLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BehaviorTreeLoader):
        """
        Dynamic initializer for BehaviorTreeLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BehaviorTreeLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BehaviorTreeLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'BehaviorTreeParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter)"""
        return 'utils.Array'._wrap(super(_BehaviorTreeLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'BehaviorTreeParameter'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter)"""
        super(_BehaviorTreeLoader, self).loadAsync(arg0, arg1, arg2, arg3)

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
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _BehaviorTreeLoader(arg0)
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'BehaviorTreeParameter') -> 'btree.BehaviorTree':
        """public com.badlogic.gdx.ai.btree.BehaviorTree com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter)"""
        return 'btree.BehaviorTree'._wrap(super(_BehaviorTreeLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_loaders.AssetLoader, self).resolve(arg0))

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader as _BehaviorTreeLoader_BehaviorTreeParameter
_BehaviorTreeParameter = _BehaviorTreeLoader_BehaviorTreeParameter.BehaviorTreeParameter
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
 
class BehaviorTreeParameter():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader.BehaviorTreeParameter"""
 
    @staticmethod
    def _wrap(java_value: _BehaviorTreeParameter) -> 'BehaviorTreeParameter':
        return BehaviorTreeParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BehaviorTreeParameter):
        """
        Dynamic initializer for BehaviorTreeParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BehaviorTreeParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BehaviorTreeParameter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object, arg1: 'BehaviorTreeParser'):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter(java.lang.Object,com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser)"""
        val = _BehaviorTreeParameter(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter()"""
        val = _BehaviorTreeParameter()
        self.__wrapper = val

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
    def __init__(self):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter()"""
        val = _BehaviorTreeParameter()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: object):
        """public com.badlogic.gdx.ai.btree.utils.BehaviorTreeLoader$BehaviorTreeParameter(java.lang.Object)"""
        val = _BehaviorTreeParameter(arg0)
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$IntegerAdapter
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters_IntegerAdapter
_IntegerAdapter = _DistributionAdapters_IntegerAdapter.IntegerAdapter
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
try:
    from pygdx.ai.utils import random
except ImportError:
    random = _import_once("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters_Adapter
_Adapter = _DistributionAdapters_Adapter.Adapter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntegerAdapter():
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.IntegerAdapter"""
 
    @staticmethod
    def _wrap(java_value: _IntegerAdapter) -> 'IntegerAdapter':
        return IntegerAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntegerAdapter):
        """
        Dynamic initializer for IntegerAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntegerAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntegerAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int._wrap(_Adapter.parseLong(arg0))

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

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float._wrap(_Adapter.parseFloat(arg0))

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
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$IntegerAdapter(java.lang.String)"""
        val = _IntegerAdapter(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float._wrap(_Adapter.parseDouble(arg0))

    @staticmethod
    @overload
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int._wrap(_Adapter.parseInteger(arg0))

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
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$Subtree
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.btree.Task as _Task
_Task = _Task
import com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser as _BehaviorTreeParser_DefaultBehaviorTreeReader_Subtree
_Subtree = _BehaviorTreeParser_DefaultBehaviorTreeReader_Subtree.DefaultBehaviorTreeReader.Subtree
import java.lang.Integer as _int
try:
    from pygdx.ai import btree
except ImportError:
    btree = _import_once("pygdx.ai.btree")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Subtree():
    """com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser.DefaultBehaviorTreeReader.Subtree"""
 
    @staticmethod
    def _wrap(java_value: _Subtree) -> 'Subtree':
        return Subtree(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Subtree):
        """
        Dynamic initializer for Subtree.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Subtree__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Subtree__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def init(self, arg0: 'Task'):
        """public void com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$Subtree.init(com.badlogic.gdx.ai.btree.Task<E>)"""
        super(_Subtree, self).init(arg0)

    @overload
    def rootTaskInstance(self) -> 'btree.Task':
        """public com.badlogic.gdx.ai.btree.Task<E> com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$Subtree.rootTaskInstance()"""
        return 'btree.Task'._wrap(super(Subtree, self).rootTaskInstance())

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

    @overload
    def isRootTree(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$Subtree.isRootTree()"""
        return bool._wrap(super(Subtree, self).isRootTree())

    @overload
    def inited(self) -> bool:
        """public boolean com.badlogic.gdx.ai.btree.utils.BehaviorTreeParser$DefaultBehaviorTreeReader$Subtree.inited()"""
        return bool._wrap(super(Subtree, self).inited())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.btree.utils.DistributionAdapters$LongAdapter
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters_LongAdapter
_LongAdapter = _DistributionAdapters_LongAdapter.LongAdapter
from builtins import float
try:
    from pygdx.ai.utils import random
except ImportError:
    random = _import_once("pygdx.ai.utils.random")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.ai.btree.utils.DistributionAdapters as _DistributionAdapters_Adapter
_Adapter = _DistributionAdapters_Adapter.Adapter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LongAdapter():
    """com.badlogic.gdx.ai.btree.utils.DistributionAdapters.LongAdapter"""
 
    @staticmethod
    def _wrap(java_value: _LongAdapter) -> 'LongAdapter':
        return LongAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongAdapter):
        """
        Dynamic initializer for LongAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def toParameters(self, arg0: 'Distribution'):
        """public abstract java.lang.String[] com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toParameters(D)"""
        pass

    @abstractmethod
    def toDistribution(self, arg0: 'String'):
        """public abstract D com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.toDistribution(java.lang.String[])"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def parseLong(arg0: str) -> int:
        """public static long com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseLong(java.lang.String)"""
        return int._wrap(_Adapter.parseLong(arg0))

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

    @staticmethod
    @overload
    def parseFloat(arg0: str) -> float:
        """public static float com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseFloat(java.lang.String)"""
        return float._wrap(_Adapter.parseFloat(arg0))

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
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.ai.btree.utils.DistributionAdapters$LongAdapter(java.lang.String)"""
        val = _LongAdapter(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def parseDouble(arg0: str) -> float:
        """public static double com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseDouble(java.lang.String)"""
        return float._wrap(_Adapter.parseDouble(arg0))

    @staticmethod
    @overload
    def parseInteger(arg0: str) -> int:
        """public static int com.badlogic.gdx.ai.btree.utils.DistributionAdapters$Adapter.parseInteger(java.lang.String)"""
        return int._wrap(_Adapter.parseInteger(arg0))

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