from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.platform.Device as __Device
__Device = __Device
 
class Device(ABC):
    """dev.ultreon.quantum.platform.Device"""
 
    @staticmethod
    def __wrap(java_value: __Device) -> 'Device':
        return Device(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Device):
        """
        Dynamic initializer for Device.
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
  
 
 
# CLASS: dev.ultreon.quantum.platform.Device
import dev.ultreon.quantum.platform.Device as __Device
__Device = __Device
 
class Device(ABC):
    """dev.ultreon.quantum.platform.Device"""
 
    @staticmethod
    def __wrap(java_value: __Device) -> 'Device':
        return Device(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Device):
        """
        Dynamic initializer for Device.
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
  
 
 
# CLASS: dev.ultreon.quantum.platform.Device 
 
 
# CLASS: dev.ultreon.quantum.platform.MouseDevice
import dev.ultreon.quantum.platform.MouseDevice as __MouseDevice
__MouseDevice = __MouseDevice
from abc import abstractmethod, ABC
 
class MouseDevice(ABC):
    """dev.ultreon.quantum.platform.MouseDevice"""
 
    @staticmethod
    def __wrap(java_value: __MouseDevice) -> 'MouseDevice':
        return MouseDevice(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MouseDevice):
        """
        Dynamic initializer for MouseDevice.
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
    def getY(self, ):
        """public abstract float dev.ultreon.quantum.platform.MouseDevice.getY()"""
        pass

    @abstractmethod
    def getX(self, ):
        """public abstract float dev.ultreon.quantum.platform.MouseDevice.getX()"""
        pass