from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.steer.utils.Path as _Path
_Path = _Path
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

 
class Path():
    """com.badlogic.gdx.ai.steer.utils.Path"""
 
    @staticmethod
    def _wrap(java_value: _Path) -> 'Path':
        return Path(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Path):
        """
        Dynamic initializer for Path.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Path__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Path__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def calculateDistance(self, arg0: 'Vector', arg1: 'PathParam'):
        """public abstract float com.badlogic.gdx.ai.steer.utils.Path.calculateDistance(T,P)"""
        pass

    @abstractmethod
    def calculateTargetPosition(self, arg0: 'Vector', arg1: 'PathParam', arg2: float):
        """public abstract void com.badlogic.gdx.ai.steer.utils.Path.calculateTargetPosition(T,P,float)"""
        pass

    @abstractmethod
    def getLength(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.utils.Path.getLength()"""
        pass

    @abstractmethod
    def getEndPoint(self, ):
        """public abstract T com.badlogic.gdx.ai.steer.utils.Path.getEndPoint()"""
        pass

    @abstractmethod
    def createParam(self, ):
        """public abstract P com.badlogic.gdx.ai.steer.utils.Path.createParam()"""
        pass

    @abstractmethod
    def getStartPoint(self, ):
        """public abstract T com.badlogic.gdx.ai.steer.utils.Path.getStartPoint()"""
        pass

    @abstractmethod
    def isOpen(self, ):
        """public abstract boolean com.badlogic.gdx.ai.steer.utils.Path.isOpen()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.Path
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.steer.utils.Path as _Path
_Path = _Path
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

 
class Path():
    """com.badlogic.gdx.ai.steer.utils.Path"""
 
    @staticmethod
    def _wrap(java_value: _Path) -> 'Path':
        return Path(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Path):
        """
        Dynamic initializer for Path.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Path__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Path__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def calculateDistance(self, arg0: 'Vector', arg1: 'PathParam'):
        """public abstract float com.badlogic.gdx.ai.steer.utils.Path.calculateDistance(T,P)"""
        pass

    @abstractmethod
    def calculateTargetPosition(self, arg0: 'Vector', arg1: 'PathParam', arg2: float):
        """public abstract void com.badlogic.gdx.ai.steer.utils.Path.calculateTargetPosition(T,P,float)"""
        pass

    @abstractmethod
    def getLength(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.utils.Path.getLength()"""
        pass

    @abstractmethod
    def getEndPoint(self, ):
        """public abstract T com.badlogic.gdx.ai.steer.utils.Path.getEndPoint()"""
        pass

    @abstractmethod
    def createParam(self, ):
        """public abstract P com.badlogic.gdx.ai.steer.utils.Path.createParam()"""
        pass

    @abstractmethod
    def getStartPoint(self, ):
        """public abstract T com.badlogic.gdx.ai.steer.utils.Path.getStartPoint()"""
        pass

    @abstractmethod
    def isOpen(self, ):
        """public abstract boolean com.badlogic.gdx.ai.steer.utils.Path.isOpen()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.Path 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.Path$PathParam
import com.badlogic.gdx.ai.steer.utils.Path as _Path_PathParam
_PathParam = _Path_PathParam.PathParam
from abc import abstractmethod, ABC
 
class PathParam():
    """com.badlogic.gdx.ai.steer.utils.Path.PathParam"""
 
    @staticmethod
    def _wrap(java_value: _PathParam) -> 'PathParam':
        return PathParam(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PathParam):
        """
        Dynamic initializer for PathParam.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PathParam__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PathParam__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setDistance(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.utils.Path$PathParam.setDistance(float)"""
        pass

    @abstractmethod
    def getDistance(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.utils.Path$PathParam.getDistance()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.RayConfiguration
import com.badlogic.gdx.ai.steer.utils.RayConfiguration as _RayConfiguration
_RayConfiguration = _RayConfiguration
from abc import abstractmethod, ABC
 
class RayConfiguration():
    """com.badlogic.gdx.ai.steer.utils.RayConfiguration"""
 
    @staticmethod
    def _wrap(java_value: _RayConfiguration) -> 'RayConfiguration':
        return RayConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RayConfiguration):
        """
        Dynamic initializer for RayConfiguration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RayConfiguration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RayConfiguration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def updateRays(self, ):
        """public abstract com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.RayConfiguration.updateRays()"""
        pass