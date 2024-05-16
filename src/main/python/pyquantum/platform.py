from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.platform.Device as _Device
_Device = _Device
 
class Device():
    """dev.ultreon.quantum.platform.Device"""
 
    @staticmethod
    def _wrap(java_value: _Device) -> 'Device':
        return Device(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Device):
        """
        Dynamic initializer for Device.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Device__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Device__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
  
 
 
# CLASS: dev.ultreon.quantum.platform.Device
import dev.ultreon.quantum.platform.Device as _Device
_Device = _Device
 
class Device():
    """dev.ultreon.quantum.platform.Device"""
 
    @staticmethod
    def _wrap(java_value: _Device) -> 'Device':
        return Device(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Device):
        """
        Dynamic initializer for Device.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Device__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Device__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
  
 
 
# CLASS: dev.ultreon.quantum.platform.Device 
 
 
# CLASS: dev.ultreon.quantum.platform.MouseDevice
import dev.ultreon.quantum.platform.MouseDevice as _MouseDevice
_MouseDevice = _MouseDevice
from abc import abstractmethod, ABC
 
class MouseDevice():
    """dev.ultreon.quantum.platform.MouseDevice"""
 
    @staticmethod
    def _wrap(java_value: _MouseDevice) -> 'MouseDevice':
        return MouseDevice(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MouseDevice):
        """
        Dynamic initializer for MouseDevice.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MouseDevice__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MouseDevice__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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