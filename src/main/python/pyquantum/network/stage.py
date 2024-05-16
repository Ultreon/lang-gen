from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.PacketData as __PacketData
__PacketData = __PacketData
from abc import abstractmethod, ABC
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.network.stage.PacketStage as __PacketStage
__PacketStage = __PacketStage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketStage(ABC):
    """dev.ultreon.quantum.network.stage.PacketStage"""
 
    @staticmethod
    def __wrap(java_value: __PacketStage) -> 'PacketStage':
        return PacketStage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketStage):
        """
        Dynamic initializer for PacketStage.
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

    @overload
    def getServerPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getServerPackets()"""
        return 'network.PacketData'.__wrap(super(PacketStage, self).getServerPackets())

    @overload
    def getClientPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.client.ClientPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getClientPackets()"""
        return 'network.PacketData'.__wrap(super(PacketStage, self).getClientPackets())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.network.stage.PacketStage
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.PacketData as __PacketData
__PacketData = __PacketData
from abc import abstractmethod, ABC
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.network.stage.PacketStage as __PacketStage
__PacketStage = __PacketStage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketStage(ABC):
    """dev.ultreon.quantum.network.stage.PacketStage"""
 
    @staticmethod
    def __wrap(java_value: __PacketStage) -> 'PacketStage':
        return PacketStage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketStage):
        """
        Dynamic initializer for PacketStage.
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

    @overload
    def getServerPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getServerPackets()"""
        return 'network.PacketData'.__wrap(super(PacketStage, self).getServerPackets())

    @overload
    def getClientPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.client.ClientPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getClientPackets()"""
        return 'network.PacketData'.__wrap(super(PacketStage, self).getClientPackets())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.network.stage.PacketStage 
 
 
# CLASS: dev.ultreon.quantum.network.stage.PacketStages
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
import dev.ultreon.quantum.network.stage.PacketStages as __PacketStages
__PacketStages = __PacketStages
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PacketStages():
    """dev.ultreon.quantum.network.stage.PacketStages"""
 
    @staticmethod
    def __wrap(java_value: __PacketStages) -> 'PacketStages':
        return PacketStages(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PacketStages):
        """
        Dynamic initializer for PacketStages.
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
 
    # public static final dev.ultreon.quantum.network.stage.LoginPacketStage dev.ultreon.quantum.network.stage.PacketStages.LOGIN
    LOGIN: 'LoginPacketStage' = __wrap(__LoginPacketStage.LOGIN)

    # public static final dev.ultreon.quantum.network.stage.InGamePacketStage dev.ultreon.quantum.network.stage.PacketStages.IN_GAME
    IN_GAME: 'InGamePacketStage' = __wrap(__InGamePacketStage.IN_GAME)


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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.network.stage.PacketStages()"""
        val = __PacketStages()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.network.stage.PacketStages()"""
        val = __PacketStages()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.network.stage.LoginPacketStage
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.network.stage.LoginPacketStage as __LoginPacketStage
__LoginPacketStage = __LoginPacketStage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.PacketData as __PacketData
__PacketData = __PacketData
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.network.stage.PacketStage as __PacketStage
__PacketStage = __PacketStage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LoginPacketStage():
    """dev.ultreon.quantum.network.stage.LoginPacketStage"""
 
    @staticmethod
    def __wrap(java_value: __LoginPacketStage) -> 'LoginPacketStage':
        return LoginPacketStage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoginPacketStage):
        """
        Dynamic initializer for LoginPacketStage.
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
    def getClientPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.client.ClientPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getClientPackets()"""
        return 'network.PacketData'.__wrap(super(PacketStage, self).getClientPackets())

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
    def getServerPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getServerPackets()"""
        return 'network.PacketData'.__wrap(super(PacketStage, self).getServerPackets())

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
    def registerPackets(self):
        """public void dev.ultreon.quantum.network.stage.LoginPacketStage.registerPackets()"""
        super(LoginPacketStage, self).registerPackets()

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
 
 
# CLASS: dev.ultreon.quantum.network.stage.InGamePacketStage
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.network.stage.InGamePacketStage as __InGamePacketStage
__InGamePacketStage = __InGamePacketStage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.network.PacketData as __PacketData
__PacketData = __PacketData
import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.network.stage.PacketStage as __PacketStage
__PacketStage = __PacketStage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InGamePacketStage():
    """dev.ultreon.quantum.network.stage.InGamePacketStage"""
 
    @staticmethod
    def __wrap(java_value: __InGamePacketStage) -> 'InGamePacketStage':
        return InGamePacketStage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InGamePacketStage):
        """
        Dynamic initializer for InGamePacketStage.
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
    def getClientPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.client.ClientPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getClientPackets()"""
        return 'network.PacketData'.__wrap(super(PacketStage, self).getClientPackets())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getServerPackets(self) -> 'network.PacketData':
        """public dev.ultreon.quantum.network.PacketData<dev.ultreon.quantum.network.server.ServerPacketHandler> dev.ultreon.quantum.network.stage.PacketStage.getServerPackets()"""
        return 'network.PacketData'.__wrap(super(PacketStage, self).getServerPackets())

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

    @override
    @overload
    def registerPackets(self):
        """public void dev.ultreon.quantum.network.stage.InGamePacketStage.registerPackets()"""
        super(InGamePacketStage, self).registerPackets()

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
        """public dev.ultreon.quantum.network.stage.InGamePacketStage()"""
        val = __InGamePacketStage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.network.stage.InGamePacketStage()"""
        val = __InGamePacketStage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))