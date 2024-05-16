from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.controllers.AbstractControllerManager as _AbstractControllerManager_ManageCurrentControllerListener
_ManageCurrentControllerListener = _AbstractControllerManager_ManageCurrentControllerListener.ManageCurrentControllerListener
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ManageCurrentControllerListener():
    """com.badlogic.gdx.controllers.AbstractControllerManager.ManageCurrentControllerListener"""
 
    @staticmethod
    def _wrap(java_value: _ManageCurrentControllerListener) -> 'ManageCurrentControllerListener':
        return ManageCurrentControllerListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ManageCurrentControllerListener):
        """
        Dynamic initializer for ManageCurrentControllerListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ManageCurrentControllerListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ManageCurrentControllerListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_ManageCurrentControllerListener, self).buttonDown(arg0, _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'AbstractControllerManager'):
        """public com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener(com.badlogic.gdx.controllers.AbstractControllerManager)"""
        val = _ManageCurrentControllerListener(arg0)
        self.__wrapper = val

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.connected(com.badlogic.gdx.controllers.Controller)"""
        super(_ManageCurrentControllerListener, self).connected(arg0)

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
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_ManageCurrentControllerListener, self).buttonUp(arg0, _int.valueOf(arg1)))

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
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool._wrap(super(_ManageCurrentControllerListener, self).axisMoved(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(_ManageCurrentControllerListener, self).disconnected(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.controllers.AbstractControllerManager as _AbstractControllerManager_ManageCurrentControllerListener
_ManageCurrentControllerListener = _AbstractControllerManager_ManageCurrentControllerListener.ManageCurrentControllerListener
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ManageCurrentControllerListener():
    """com.badlogic.gdx.controllers.AbstractControllerManager.ManageCurrentControllerListener"""
 
    @staticmethod
    def _wrap(java_value: _ManageCurrentControllerListener) -> 'ManageCurrentControllerListener':
        return ManageCurrentControllerListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ManageCurrentControllerListener):
        """
        Dynamic initializer for ManageCurrentControllerListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ManageCurrentControllerListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ManageCurrentControllerListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_ManageCurrentControllerListener, self).buttonDown(arg0, _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'AbstractControllerManager'):
        """public com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener(com.badlogic.gdx.controllers.AbstractControllerManager)"""
        val = _ManageCurrentControllerListener(arg0)
        self.__wrapper = val

    @override
    @overload
    def connected(self, arg0: 'Controller'):
        """public void com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.connected(com.badlogic.gdx.controllers.Controller)"""
        super(_ManageCurrentControllerListener, self).connected(arg0)

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
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_ManageCurrentControllerListener, self).buttonUp(arg0, _int.valueOf(arg1)))

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
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool._wrap(super(_ManageCurrentControllerListener, self).axisMoved(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(_ManageCurrentControllerListener, self).disconnected(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.controllers.AbstractControllerManager$ManageCurrentControllerListener 
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerAdapter
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.controllers.ControllerAdapter as _ControllerAdapter
_ControllerAdapter = _ControllerAdapter
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ControllerAdapter():
    """com.badlogic.gdx.controllers.ControllerAdapter"""
 
    @staticmethod
    def _wrap(java_value: _ControllerAdapter) -> 'ControllerAdapter':
        return ControllerAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ControllerAdapter):
        """
        Dynamic initializer for ControllerAdapter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ControllerAdapter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ControllerAdapter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def disconnected(self, arg0: 'Controller'):
        """public void com.badlogic.gdx.controllers.ControllerAdapter.disconnected(com.badlogic.gdx.controllers.Controller)"""
        super(_ControllerAdapter, self).disconnected(arg0)

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
    def connected(self, arg0: 'Controller'):
        """public void com.badlogic.gdx.controllers.ControllerAdapter.connected(com.badlogic.gdx.controllers.Controller)"""
        super(_ControllerAdapter, self).connected(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def axisMoved(self, arg0: 'Controller', arg1: int, arg2: float) -> bool:
        """public boolean com.badlogic.gdx.controllers.ControllerAdapter.axisMoved(com.badlogic.gdx.controllers.Controller,int,float)"""
        return bool._wrap(super(_ControllerAdapter, self).axisMoved(arg0, _int.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def buttonUp(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.controllers.ControllerAdapter.buttonUp(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_ControllerAdapter, self).buttonUp(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.controllers.ControllerAdapter()"""
        val = _ControllerAdapter()
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
    def buttonDown(self, arg0: 'Controller', arg1: int) -> bool:
        """public boolean com.badlogic.gdx.controllers.ControllerAdapter.buttonDown(com.badlogic.gdx.controllers.Controller,int)"""
        return bool._wrap(super(_ControllerAdapter, self).buttonDown(arg0, _int.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.controllers.ControllerAdapter()"""
        val = _ControllerAdapter()
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
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerManager
import com.badlogic.gdx.controllers.ControllerManager as _ControllerManager
_ControllerManager = _ControllerManager
from abc import abstractmethod, ABC
 
class ControllerManager():
    """com.badlogic.gdx.controllers.ControllerManager"""
 
    @staticmethod
    def _wrap(java_value: _ControllerManager) -> 'ControllerManager':
        return ControllerManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ControllerManager):
        """
        Dynamic initializer for ControllerManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ControllerManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ControllerManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.controllers.Controller
import com.badlogic.gdx.controllers.Controller as _Controller
_Controller = _Controller
from abc import abstractmethod, ABC
 
class Controller():
    """com.badlogic.gdx.controllers.Controller"""
 
    @staticmethod
    def _wrap(java_value: _Controller) -> 'Controller':
        return Controller(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Controller):
        """
        Dynamic initializer for Controller.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Controller__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Controller__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerPowerLevel
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
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import com.badlogic.gdx.controllers.ControllerPowerLevel as _ControllerPowerLevel
_ControllerPowerLevel = _ControllerPowerLevel
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ControllerPowerLevel():
    """com.badlogic.gdx.controllers.ControllerPowerLevel"""
 
    @staticmethod
    def _wrap(java_value: _ControllerPowerLevel) -> 'ControllerPowerLevel':
        return ControllerPowerLevel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ControllerPowerLevel):
        """
        Dynamic initializer for ControllerPowerLevel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ControllerPowerLevel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ControllerPowerLevel__wrapper":
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ControllerPowerLevel':
        """public static com.badlogic.gdx.controllers.ControllerPowerLevel com.badlogic.gdx.controllers.ControllerPowerLevel.valueOf(java.lang.String)"""
        return ControllerPowerLevel._wrap(_ControllerPowerLevel.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['ControllerPowerLevel']:
        """public static com.badlogic.gdx.controllers.ControllerPowerLevel[] com.badlogic.gdx.controllers.ControllerPowerLevel.values()"""
        return List[ControllerPowerLevel]._wrap(_ControllerPowerLevel.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerManagerStub
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
import com.badlogic.gdx.controllers.ControllerManagerStub as _ControllerManagerStub
_ControllerManagerStub = _ControllerManagerStub
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.controllers.Controller as _Controller
_Controller = _Controller
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.controllers.AbstractControllerManager as _AbstractControllerManager
_AbstractControllerManager = _AbstractControllerManager
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ControllerManagerStub():
    """com.badlogic.gdx.controllers.ControllerManagerStub"""
 
    @staticmethod
    def _wrap(java_value: _ControllerManagerStub) -> 'ControllerManagerStub':
        return ControllerManagerStub(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ControllerManagerStub):
        """
        Dynamic initializer for ControllerManagerStub.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ControllerManagerStub__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ControllerManagerStub__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getControllers(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.Controller> com.badlogic.gdx.controllers.AbstractControllerManager.getControllers()"""
        return 'utils.Array'._wrap(super(AbstractControllerManager, self).getControllers())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.controllers.ControllerManagerStub()"""
        val = _ControllerManagerStub()
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

    @override
    @overload
    def removeListener(self, arg0: 'ControllerListener'):
        """public void com.badlogic.gdx.controllers.ControllerManagerStub.removeListener(com.badlogic.gdx.controllers.ControllerListener)"""
        super(_ControllerManagerStub, self).removeListener(arg0)

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
    def getListeners(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.ControllerListener> com.badlogic.gdx.controllers.ControllerManagerStub.getListeners()"""
        return 'utils.Array'._wrap(super(ControllerManagerStub, self).getListeners())

    @override
    @overload
    def getCurrentController(self) -> 'Controller':
        """public com.badlogic.gdx.controllers.Controller com.badlogic.gdx.controllers.AbstractControllerManager.getCurrentController()"""
        return 'Controller'._wrap(super(AbstractControllerManager, self).getCurrentController())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.controllers.ControllerManagerStub()"""
        val = _ControllerManagerStub()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def addListener(self, arg0: 'ControllerListener'):
        """public void com.badlogic.gdx.controllers.ControllerManagerStub.addListener(com.badlogic.gdx.controllers.ControllerListener)"""
        super(_ControllerManagerStub, self).addListener(arg0)

    @override
    @overload
    def clearListeners(self):
        """public void com.badlogic.gdx.controllers.ControllerManagerStub.clearListeners()"""
        super(ControllerManagerStub, self).clearListeners()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.controllers.Controllers
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
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.controllers.Controller as _Controller
_Controller = _Controller
import java.lang.Integer as _int
import com.badlogic.gdx.controllers.Controllers as _Controllers
_Controllers = _Controllers
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Controllers():
    """com.badlogic.gdx.controllers.Controllers"""
 
    @staticmethod
    def _wrap(java_value: _Controllers) -> 'Controllers':
        return Controllers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Controllers):
        """
        Dynamic initializer for Controllers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Controllers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Controllers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getCurrent() -> 'Controller':
        """public static com.badlogic.gdx.controllers.Controller com.badlogic.gdx.controllers.Controllers.getCurrent()"""
        return Controller._wrap(_Controllers.getCurrent())

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
    def __init__(self, ):
        """public com.badlogic.gdx.controllers.Controllers()"""
        val = _Controllers()
        self.__wrapper = val

    @staticmethod
    @overload
    def removeListener(arg0: 'ControllerListener'):
        """public static void com.badlogic.gdx.controllers.Controllers.removeListener(com.badlogic.gdx.controllers.ControllerListener)"""
        _Controllers.removeListener(arg0)

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

    @staticmethod
    @overload
    def getListeners() -> 'utils.Array':
        """public static com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.ControllerListener> com.badlogic.gdx.controllers.Controllers.getListeners()"""
        return utils.Array._wrap(_Controllers.getListeners())

    @staticmethod
    @overload
    def getControllers() -> 'utils.Array':
        """public static com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.Controller> com.badlogic.gdx.controllers.Controllers.getControllers()"""
        return utils.Array._wrap(_Controllers.getControllers())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.controllers.Controllers()"""
        val = _Controllers()
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

        @staticmethod
        @overload
        def clearListeners():
            """public static void com.badlogic.gdx.controllers.Controllers.clearListeners()"""
            _Controllers.clearListeners()

    @staticmethod
    @overload
    def addListener(arg0: 'ControllerListener'):
        """public static void com.badlogic.gdx.controllers.Controllers.addListener(com.badlogic.gdx.controllers.ControllerListener)"""
        _Controllers.addListener(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerMapping
import com.badlogic.gdx.controllers.ControllerMapping as _ControllerMapping
_ControllerMapping = _ControllerMapping
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
 
class ControllerMapping():
    """com.badlogic.gdx.controllers.ControllerMapping"""
 
    @staticmethod
    def _wrap(java_value: _ControllerMapping) -> 'ControllerMapping':
        return ControllerMapping(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ControllerMapping):
        """
        Dynamic initializer for ControllerMapping.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ControllerMapping__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ControllerMapping__wrapper":
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
 
 
# CLASS: com.badlogic.gdx.controllers.AbstractControllerManager
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.controllers.ControllerManager as _ControllerManager
_ControllerManager = _ControllerManager
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
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.controllers.Controller as _Controller
_Controller = _Controller
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.controllers.AbstractControllerManager as _AbstractControllerManager
_AbstractControllerManager = _AbstractControllerManager
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractControllerManager():
    """com.badlogic.gdx.controllers.AbstractControllerManager"""
 
    @staticmethod
    def _wrap(java_value: _AbstractControllerManager) -> 'AbstractControllerManager':
        return AbstractControllerManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractControllerManager):
        """
        Dynamic initializer for AbstractControllerManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractControllerManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractControllerManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.controllers.AbstractControllerManager()"""
        val = _AbstractControllerManager()
        self.__wrapper = val

    @override
    @overload
    def getControllers(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.Controller> com.badlogic.gdx.controllers.AbstractControllerManager.getControllers()"""
        return 'utils.Array'._wrap(super(AbstractControllerManager, self).getControllers())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.controllers.AbstractControllerManager()"""
        val = _AbstractControllerManager()
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def removeListener(self, arg0: 'ControllerListener'):
        """public abstract void com.badlogic.gdx.controllers.ControllerManager.removeListener(com.badlogic.gdx.controllers.ControllerListener)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def getListeners(self, ):
        """public abstract com.badlogic.gdx.utils.Array<com.badlogic.gdx.controllers.ControllerListener> com.badlogic.gdx.controllers.ControllerManager.getListeners()"""
        pass

    @override
    @overload
    def getCurrentController(self) -> 'Controller':
        """public com.badlogic.gdx.controllers.Controller com.badlogic.gdx.controllers.AbstractControllerManager.getCurrentController()"""
        return 'Controller'._wrap(super(AbstractControllerManager, self).getCurrentController())

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
 
 
# CLASS: com.badlogic.gdx.controllers.ControllerListener
import com.badlogic.gdx.controllers.ControllerListener as _ControllerListener
_ControllerListener = _ControllerListener
from abc import abstractmethod, ABC
 
class ControllerListener():
    """com.badlogic.gdx.controllers.ControllerListener"""
 
    @staticmethod
    def _wrap(java_value: _ControllerListener) -> 'ControllerListener':
        return ControllerListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ControllerListener):
        """
        Dynamic initializer for ControllerListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ControllerListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ControllerListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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