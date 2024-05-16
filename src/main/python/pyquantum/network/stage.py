from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.PacketData as _PacketData
_PacketData = _PacketData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import dev.ultreon.quantum.network.stage.PacketStage as _PacketStage
_PacketStage = _PacketStage
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketStage():
    """dev.ultreon.quantum.network.stage.PacketStage"""
 
    @staticmethod
    def _wrap(java_value: _PacketStage) -> 'PacketStage':
        return PacketStage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketStage):
        """
        Dynamic initializer for PacketStage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketStage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketStage__wrapper":
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
    def getServerPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getServerPackets()"""
        return 'network.PacketData'._wrap(super(PacketStage, self).getServerPackets())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getClientPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.client.ClientPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getClientPackets()"""
        return 'network.PacketData'._wrap(super(PacketStage, self).getClientPackets())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def registerPackets(self, ):
        """public abstract void dev.ultreon.quantum.network.stage.PacketStage.registerPackets()"""
        pass

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

 
 
 
# CLASS: dev.ultreon.quantum.network.stage.PacketStage
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.PacketData as _PacketData
_PacketData = _PacketData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import dev.ultreon.quantum.network.stage.PacketStage as _PacketStage
_PacketStage = _PacketStage
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PacketStage():
    """dev.ultreon.quantum.network.stage.PacketStage"""
 
    @staticmethod
    def _wrap(java_value: _PacketStage) -> 'PacketStage':
        return PacketStage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketStage):
        """
        Dynamic initializer for PacketStage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketStage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketStage__wrapper":
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
    def getServerPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getServerPackets()"""
        return 'network.PacketData'._wrap(super(PacketStage, self).getServerPackets())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getClientPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.client.ClientPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getClientPackets()"""
        return 'network.PacketData'._wrap(super(PacketStage, self).getClientPackets())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def registerPackets(self, ):
        """public abstract void dev.ultreon.quantum.network.stage.PacketStage.registerPackets()"""
        pass

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

 
 
 
# CLASS: dev.ultreon.quantum.network.stage.PacketStage 
 
 
# CLASS: dev.ultreon.quantum.network.stage.PacketStages
from builtins import str
import dev.ultreon.quantum.network.stage.PacketStages as _PacketStages
_PacketStages = _PacketStages
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
 
class PacketStages():
    """dev.ultreon.quantum.network.stage.PacketStages"""
 
    @staticmethod
    def _wrap(java_value: _PacketStages) -> 'PacketStages':
        return PacketStages(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PacketStages):
        """
        Dynamic initializer for PacketStages.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PacketStages__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PacketStages__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.network.stage.LoginPacketStage dev.ultreon.quantum.network.stage.PacketStages.LOGIN
    LOGIN: 'LoginPacketStage' = _wrap(_LoginPacketStage.LOGIN)

    # public static final dev.ultreon.quantum.network.stage.InGamePacketStage dev.ultreon.quantum.network.stage.PacketStages.IN_GAME
    IN_GAME: 'InGamePacketStage' = _wrap(_InGamePacketStage.IN_GAME)


    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.stage.PacketStages()"""
        val = _PacketStages()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.stage.PacketStages()"""
        val = _PacketStages()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.network.stage.LoginPacketStage
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.PacketData as _PacketData
_PacketData = _PacketData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import dev.ultreon.quantum.network.stage.PacketStage as _PacketStage
_PacketStage = _PacketStage
import java.lang.Integer as _int
import dev.ultreon.quantum.network.stage.LoginPacketStage as _LoginPacketStage
_LoginPacketStage = _LoginPacketStage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LoginPacketStage():
    """dev.ultreon.quantum.network.stage.LoginPacketStage"""
 
    @staticmethod
    def _wrap(java_value: _LoginPacketStage) -> 'LoginPacketStage':
        return LoginPacketStage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoginPacketStage):
        """
        Dynamic initializer for LoginPacketStage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoginPacketStage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoginPacketStage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getServerPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getServerPackets()"""
        return 'network.PacketData'._wrap(super(PacketStage, self).getServerPackets())

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
    def registerPackets(self):
        """public void dev.ultreon.quantum.network.stage.LoginPacketStage.registerPackets()"""
        super(LoginPacketStage, self).registerPackets()

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

    @override
    @overload
    def getClientPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.client.ClientPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getClientPackets()"""
        return 'network.PacketData'._wrap(super(PacketStage, self).getClientPackets())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.network.stage.InGamePacketStage
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.network.PacketData as _PacketData
_PacketData = _PacketData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import dev.ultreon.quantum.network.stage.PacketStage as _PacketStage
_PacketStage = _PacketStage
import java.lang.Integer as _int
import dev.ultreon.quantum.network.stage.InGamePacketStage as _InGamePacketStage
_InGamePacketStage = _InGamePacketStage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InGamePacketStage():
    """dev.ultreon.quantum.network.stage.InGamePacketStage"""
 
    @staticmethod
    def _wrap(java_value: _InGamePacketStage) -> 'InGamePacketStage':
        return InGamePacketStage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InGamePacketStage):
        """
        Dynamic initializer for InGamePacketStage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InGamePacketStage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InGamePacketStage__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.stage.InGamePacketStage()"""
        val = _InGamePacketStage()
        self.__wrapper = val

    @override
    @overload
    def registerPackets(self):
        """public void dev.ultreon.quantum.network.stage.InGamePacketStage.registerPackets()"""
        super(InGamePacketStage, self).registerPackets()

    @override
    @overload
    def getServerPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getServerPackets()"""
        return 'network.PacketData'._wrap(super(PacketStage, self).getServerPackets())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.stage.InGamePacketStage()"""
        val = _InGamePacketStage()
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getClientPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.client.ClientPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getClientPackets()"""
        return 'network.PacketData'._wrap(super(PacketStage, self).getClientPackets())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())