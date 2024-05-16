from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.controllers.Controllers as __Controllers
__Controllers = __Controllers
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.controllers.Controller as __Controller
__Controller = __Controller
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Controllers():
    """com.badlogic.gdx.controllers.Controllers"""
 
    @staticmethod
    def __wrap(java_value: __Controllers) -> 'Controllers':
        return Controllers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Controllers):
        """
        Dynamic initializer for Controllers.
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
        def clearListeners():
            """public static void com.badlogic.gdx.controllers.Controllers.clearListeners()"""
            __Controllers.clearListeners()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def addListener(arg0: 'ControllerListener'):
        """public static void com.badlogic.gdx.controllers.Controllers.addListener(com.badlogic.gdx.controllers.ControllerListener)"""
        __Controllers.addListener(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def removeListener(arg0: 'ControllerListener'):
        """public static void com.badlogic.gdx.controllers.Controllers.removeListener(com.badlogic.gdx.controllers.ControllerListener)"""
        __Controllers.removeListener(arg0)

    @staticmethod
    @overload
    def getControllers() -> 'utils.Array':
        """public static com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.Controller> com.badlogic.gdx.controllers.Controllers.getControllers()"""
        return utils.Array.__wrap(__Controllers.getControllers())

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
    def __init__(self):
        """public com.badlogic.gdx.controllers.Controllers()"""
        val = __Controllers()
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
    def __init__(self, ):
        """public com.badlogic.gdx.controllers.Controllers()"""
        val = __Controllers()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getListeners() -> 'utils.Array':
        """public static com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.ControllerListener> com.badlogic.gdx.controllers.Controllers.getListeners()"""
        return utils.Array.__wrap(__Controllers.getListeners())

    @staticmethod
    @overload
    def getCurrent() -> 'Controller':
        """public static com.badlogic.gdx.controllers.Controller com.badlogic.gdx.controllers.Controllers.getCurrent()"""
        return Controller.__wrap(__Controllers.getCurrent())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.controllers.Controllers
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.controllers.Controllers as __Controllers
__Controllers = __Controllers
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.controllers.Controller as __Controller
__Controller = __Controller
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Controllers():
    """com.badlogic.gdx.controllers.Controllers"""
 
    @staticmethod
    def __wrap(java_value: __Controllers) -> 'Controllers':
        return Controllers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Controllers):
        """
        Dynamic initializer for Controllers.
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
        def clearListeners():
            """public static void com.badlogic.gdx.controllers.Controllers.clearListeners()"""
            __Controllers.clearListeners()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def addListener(arg0: 'ControllerListener'):
        """public static void com.badlogic.gdx.controllers.Controllers.addListener(com.badlogic.gdx.controllers.ControllerListener)"""
        __Controllers.addListener(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def removeListener(arg0: 'ControllerListener'):
        """public static void com.badlogic.gdx.controllers.Controllers.removeListener(com.badlogic.gdx.controllers.ControllerListener)"""
        __Controllers.removeListener(arg0)

    @staticmethod
    @overload
    def getControllers() -> 'utils.Array':
        """public static com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.Controller> com.badlogic.gdx.controllers.Controllers.getControllers()"""
        return utils.Array.__wrap(__Controllers.getControllers())

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
    def __init__(self):
        """public com.badlogic.gdx.controllers.Controllers()"""
        val = __Controllers()
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
    def __init__(self, ):
        """public com.badlogic.gdx.controllers.Controllers()"""
        val = __Controllers()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getListeners() -> 'utils.Array':
        """public static com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.ControllerListener> com.badlogic.gdx.controllers.Controllers.getListeners()"""
        return utils.Array.__wrap(__Controllers.getListeners())

    @staticmethod
    @overload
    def getCurrent() -> 'Controller':
        """public static com.badlogic.gdx.controllers.Controller com.badlogic.gdx.controllers.Controllers.getCurrent()"""
        return Controller.__wrap(__Controllers.getCurrent())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.controllers.Controllers 
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerPowerLevel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import com.badlogic.gdx.controllers.ControllerPowerLevel as __ControllerPowerLevel
__ControllerPowerLevel = __ControllerPowerLevel
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
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
 
class ControllerPowerLevel(__Enum, Enum):
    """com.badlogic.gdx.controllers.ControllerPowerLevel"""
 
    @staticmethod
    def __wrap(java_value: __ControllerPowerLevel) -> 'ControllerPowerLevel':
        return ControllerPowerLevel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ControllerPowerLevel):
        """
        Dynamic initializer for ControllerPowerLevel.
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

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ControllerPowerLevel':
        """public static com.badlogic.gdx.controllers.ControllerPowerLevel com.badlogic.gdx.controllers.ControllerPowerLevel.valueOf(java.lang.String)"""
        return ControllerPowerLevel.__wrap(__ControllerPowerLevel.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['ControllerPowerLevel']:
        """public static com.badlogic.gdx.controllers.ControllerPowerLevel[] com.badlogic.gdx.controllers.ControllerPowerLevel.values()"""
        return List[ControllerPowerLevel].__wrap(__ControllerPowerLevel.values())

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
 
 
# CLASS: com.badlogic.gdx.controllers.Controller
import com.badlogic.gdx.controllers.Controller as __Controller
__Controller = __Controller
from abc import abstractmethod, ABC
 
class Controller(ABC):
    """com.badlogic.gdx.controllers.Controller"""
 
    @staticmethod
    def __wrap(java_value: __Controller) -> 'Controller':
        return Controller(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Controller):
        """
        Dynamic initializer for Controller.
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
    def getAxis(self, arg0: int):
        """public abstract float com.badlogic.gdx.controllers.Controller.getAxis(int)"""
        pass

    @abstractmethod
    def cancelVibration(self, ):
        """public abstract void com.badlogic.gdx.controllers.Controller.cancelVibration()"""
        pass

    @abstractmethod
    def isConnected(self, ):
        """public abstract boolean com.badlogic.gdx.controllers.Controller.isConnected()"""
        pass

    @abstractmethod
    def startVibration(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.controllers.Controller.startVibration(int,float)"""
        pass

    @abstractmethod
    def addListener(self, arg0: 'ControllerListener'):
        """public abstract void com.badlogic.gdx.controllers.Controller.addListener(com.badlogic.gdx.controllers.ControllerListener)"""
        pass

    @abstractmethod
    def getAxisCount(self, ):
        """public abstract int com.badlogic.gdx.controllers.Controller.getAxisCount()"""
        pass

    @abstractmethod
    def getPowerLevel(self, ):
        """public abstract com.badlogic.gdx.controllers.ControllerPowerLevel com.badlogic.gdx.controllers.Controller.getPowerLevel()"""
        pass

    @abstractmethod
    def getMaxButtonIndex(self, ):
        """public abstract int com.badlogic.gdx.controllers.Controller.getMaxButtonIndex()"""
        pass

    @abstractmethod
    def getButton(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.controllers.Controller.getButton(int)"""
        pass

    @abstractmethod
    def getUniqueId(self, ):
        """public abstract java.lang.String com.badlogic.gdx.controllers.Controller.getUniqueId()"""
        pass

    @abstractmethod
    def setPlayerIndex(self, arg0: int):
        """public abstract void com.badlogic.gdx.controllers.Controller.setPlayerIndex(int)"""
        pass

    @abstractmethod
    def getPlayerIndex(self, ):
        """public abstract int com.badlogic.gdx.controllers.Controller.getPlayerIndex()"""
        pass

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String com.badlogic.gdx.controllers.Controller.getName()"""
        pass

    @abstractmethod
    def supportsPlayerIndex(self, ):
        """public abstract boolean com.badlogic.gdx.controllers.Controller.supportsPlayerIndex()"""
        pass

    @abstractmethod
    def removeListener(self, arg0: 'ControllerListener'):
        """public abstract void com.badlogic.gdx.controllers.Controller.removeListener(com.badlogic.gdx.controllers.ControllerListener)"""
        pass

    @abstractmethod
    def getMinButtonIndex(self, ):
        """public abstract int com.badlogic.gdx.controllers.Controller.getMinButtonIndex()"""
        pass

    @abstractmethod
    def getMapping(self, ):
        """public abstract com.badlogic.gdx.controllers.ControllerMapping com.badlogic.gdx.controllers.Controller.getMapping()"""
        pass

    @abstractmethod
    def canVibrate(self, ):
        """public abstract boolean com.badlogic.gdx.controllers.Controller.canVibrate()"""
        pass

    @abstractmethod
    def isVibrating(self, ):
        """public abstract boolean com.badlogic.gdx.controllers.Controller.isVibrating()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.controllers.AbstractControllerManager as __AbstractControllerManager_ManageCurrentControllerListener
__ManageCurrentControllerListener = __AbstractControllerManager_ManageCurrentControllerListener.ManageCurrentControllerListener
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ManageCurrentControllerListener(__ControllerAdapter, ControllerAdapter):
    """com.badlogic.gdx.controllers.AbstractControllerManager.ManageCurrentControllerListener"""
 
    @staticmethod
    def __wrap(java_value: __ManageCurrentControllerListener) -> 'ManageCurrentControllerListener':
        return ManageCurrentControllerListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ManageCurrentControllerListener):
        """
        Dynamic initializer for ManageCurrentControllerListener.
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
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__ManageCurrentControllerListener, self).buttonDown(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool.__wrap(super(__ManageCurrentControllerListener, self).axisMoved(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'AbstractControllerManager'):
        """public com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener(com.badlogic.gdx.controllers.AbstractControllerManager)"""
        val = __ManageCurrentControllerListener(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.connected(com.badlogic.gdx.controllers.Controller)"""
        super(__ManageCurrentControllerListener, self).connected(arg0)

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
    def disconnected(self, arg0: 'Controller'):
        """public void com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(__ManageCurrentControllerListener, self).disconnected(arg0)

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
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__ManageCurrentControllerListener, self).buttonUp(arg0, __int.valueOf(arg1)))

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
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerManagerStub
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.controllers.AbstractControllerManager as __AbstractControllerManager
__AbstractControllerManager = __AbstractControllerManager
import com.badlogic.gdx.controllers.ControllerManagerStub as __ControllerManagerStub
__ControllerManagerStub = __ControllerManagerStub
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.controllers.Controller as __Controller
__Controller = __Controller
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ControllerManagerStub(__AbstractControllerManager, AbstractControllerManager):
    """com.badlogic.gdx.controllers.ControllerManagerStub"""
 
    @staticmethod
    def __wrap(java_value: __ControllerManagerStub) -> 'ControllerManagerStub':
        return ControllerManagerStub(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ControllerManagerStub):
        """
        Dynamic initializer for ControllerManagerStub.
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
    def __init__(self, ):
        """public com.badlogic.gdx.controllers.ControllerManagerStub()"""
        val = __ControllerManagerStub()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def addListener(self, arg0: 'ControllerListener'):
        """public void com.badlogic.gdx.controllers.ControllerManagerStub.addListener(com.badlogic.gdx.controllers.ControllerListener)"""
        super(__ControllerManagerStub, self).addListener(arg0)

    @override
    @overload
    def getListeners(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.ControllerListener> com.badlogic.gdx.controllers.ControllerManagerStub.getListeners()"""
        return 'utils.Array'.__wrap(super(ControllerManagerStub, self).getListeners())

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
        """public com.badlogic.gdx.controllers.ControllerManagerStub()"""
        val = __ControllerManagerStub()
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
    def removeListener(self, arg0: 'ControllerListener'):
        """public void com.badlogic.gdx.controllers.ControllerManagerStub.removeListener(com.badlogic.gdx.controllers.ControllerListener)"""
        super(__ControllerManagerStub, self).removeListener(arg0)

    @override
    @overload
    def getCurrentController(self) -> 'Controller':
        """public com.badlogic.gdx.controllers.Controller com.badlogic.gdx.controllers.AbstractControllerManager.getCurrentController()"""
        return 'Controller'.__wrap(super(AbstractControllerManager, self).getCurrentController())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getControllers(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.Controller> com.badlogic.gdx.controllers.AbstractControllerManager.getControllers()"""
        return 'utils.Array'.__wrap(super(AbstractControllerManager, self).getControllers())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def clearListeners(self):
        """public void com.badlogic.gdx.controllers.ControllerManagerStub.clearListeners()"""
        super(ControllerManagerStub, self).clearListeners()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerManager
import com.badlogic.gdx.controllers.ControllerManager as __ControllerManager
__ControllerManager = __ControllerManager
from abc import abstractmethod, ABC
 
class ControllerManager(ABC):
    """com.badlogic.gdx.controllers.ControllerManager"""
 
    @staticmethod
    def __wrap(java_value: __ControllerManager) -> 'ControllerManager':
        return ControllerManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ControllerManager):
        """
        Dynamic initializer for ControllerManager.
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
    def clearListeners(self, ):
        """public abstract void com.badlogic.gdx.controllers.ControllerManager.clearListeners()"""
        pass

    @abstractmethod
    def addListener(self, arg0: 'ControllerListener'):
        """public abstract void com.badlogic.gdx.controllers.ControllerManager.addListener(com.badlogic.gdx.controllers.ControllerListener)"""
        pass

    @abstractmethod
    def getListeners(self, ):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.ControllerListener> com.badlogic.gdx.controllers.ControllerManager.getListeners()"""
        pass

    @abstractmethod
    def removeListener(self, arg0: 'ControllerListener'):
        """public abstract void com.badlogic.gdx.controllers.ControllerManager.removeListener(com.badlogic.gdx.controllers.ControllerListener)"""
        pass

    @abstractmethod
    def getCurrentController(self, ):
        """public abstract com.badlogic.gdx.controllers.Controller com.badlogic.gdx.controllers.ControllerManager.getCurrentController()"""
        pass

    @abstractmethod
    def getControllers(self, ):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.Controller> com.badlogic.gdx.controllers.ControllerManager.getControllers()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.controllers.AbstractControllerManager
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.controllers.AbstractControllerManager as __AbstractControllerManager
__AbstractControllerManager = __AbstractControllerManager
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.controllers.Controller as __Controller
__Controller = __Controller
import java.lang.Integer as __int
import com.badlogic.gdx.controllers.ControllerManager as __ControllerManager
__ControllerManager = __ControllerManager
from builtins import bool
from builtins import int
 
class AbstractControllerManager(ABC, __ControllerManager, ControllerManager):
    """com.badlogic.gdx.controllers.AbstractControllerManager"""
 
    @staticmethod
    def __wrap(java_value: __AbstractControllerManager) -> 'AbstractControllerManager':
        return AbstractControllerManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractControllerManager):
        """
        Dynamic initializer for AbstractControllerManager.
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

    @abstractmethod
    def removeListener(self, arg0: 'ControllerListener'):
        """public abstract void com.badlogic.gdx.controllers.ControllerManager.removeListener(com.badlogic.gdx.controllers.ControllerListener)"""
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
    def clearListeners(self, ):
        """public abstract void com.badlogic.gdx.controllers.ControllerManager.clearListeners()"""
        pass

    @abstractmethod
    def addListener(self, arg0: 'ControllerListener'):
        """public abstract void com.badlogic.gdx.controllers.ControllerManager.addListener(com.badlogic.gdx.controllers.ControllerListener)"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.controllers.AbstractControllerManager()"""
        val = __AbstractControllerManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getCurrentController(self) -> 'Controller':
        """public com.badlogic.gdx.controllers.Controller com.badlogic.gdx.controllers.AbstractControllerManager.getCurrentController()"""
        return 'Controller'.__wrap(super(AbstractControllerManager, self).getCurrentController())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def getListeners(self, ):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.ControllerListener> com.badlogic.gdx.controllers.ControllerManager.getListeners()"""
        pass

    @override
    @overload
    def getControllers(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.Controller> com.badlogic.gdx.controllers.AbstractControllerManager.getControllers()"""
        return 'utils.Array'.__wrap(super(AbstractControllerManager, self).getControllers())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.controllers.AbstractControllerManager()"""
        val = __AbstractControllerManager()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerMapping
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
import com.badlogic.gdx.controllers.ControllerMapping as __ControllerMapping
__ControllerMapping = __ControllerMapping
from builtins import int
 
class ControllerMapping():
    """com.badlogic.gdx.controllers.ControllerMapping"""
 
    @staticmethod
    def __wrap(java_value: __ControllerMapping) -> 'ControllerMapping':
        return ControllerMapping(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ControllerMapping):
        """
        Dynamic initializer for ControllerMapping.
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
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerAdapter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.controllers.ControllerAdapter as __ControllerAdapter
__ControllerAdapter = __ControllerAdapter
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ControllerAdapter(__ControllerListener, ControllerListener):
    """com.badlogic.gdx.controllers.ControllerAdapter"""
 
    @staticmethod
    def __wrap(java_value: __ControllerAdapter) -> 'ControllerAdapter':
        return ControllerAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ControllerAdapter):
        """
        Dynamic initializer for ControllerAdapter.
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
        """public com.badlogic.gdx.controllers.ControllerAdapter()"""
        val = __ControllerAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void com.badlogic.gdx.controllers.ControllerAdapter.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(__ControllerAdapter, self).disconnected(arg0)

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.controllers.ControllerAdapter.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool.__wrap(super(__ControllerAdapter, self).axisMoved(arg0, __int.valueOf(arg1), __float.valueOf(arg2)))

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
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.controllers.ControllerAdapter.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__ControllerAdapter, self).buttonDown(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.controllers.ControllerAdapter()"""
        val = __ControllerAdapter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.controllers.ControllerAdapter.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool.__wrap(super(__ControllerAdapter, self).buttonUp(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void com.badlogic.gdx.controllers.ControllerAdapter.connected(com.badlogic.gdx.controllers.Controller)"""
        super(__ControllerAdapter, self).connected(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerListener
import com.badlogic.gdx.controllers.ControllerListener as __ControllerListener
__ControllerListener = __ControllerListener
from abc import abstractmethod, ABC
 
class ControllerListener(ABC):
    """com.badlogic.gdx.controllers.ControllerListener"""
 
    @staticmethod
    def __wrap(java_value: __ControllerListener) -> 'ControllerListener':
        return ControllerListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ControllerListener):
        """
        Dynamic initializer for ControllerListener.
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
    def connected(self, arg0: 'Controller'):
        """public abstract void com.badlogic.gdx.controllers.ControllerListener.connected(com.badlogic.gdx.controllers.Controller)"""
        pass

    @abstractmethod
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float):
        """public abstract boolean com.badlogic.gdx.controllers.ControllerListener.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        pass

    @abstractmethod
    def disconnected(self, arg0: 'Controller'):
        """public abstract void com.badlogic.gdx.controllers.ControllerListener.disconnected(com.badlogic.gdx.controllers.Controller)"""
        pass

    @abstractmethod
    def buttonUp(self, arg0: 'Controller', arg1: int):
        """public abstract boolean com.badlogic.gdx.controllers.ControllerListener.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        pass

    @abstractmethod
    def buttonDown(self, arg0: 'Controller', arg1: int):
        """public abstract boolean com.badlogic.gdx.controllers.ControllerListener.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        pass