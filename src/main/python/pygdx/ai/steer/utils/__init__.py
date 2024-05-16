from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.utils.Path as __Path
__Path = __Path
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

 
class Path(ABC):
    """com.badlogic.gdx.ai.steer.utils.Path"""
 
    @staticmethod
    def __wrap(java_value: __Path) -> 'Path':
        return Path(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Path):
        """
        Dynamic initializer for Path.
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
    def createParam(self, ):
        """public abstract P com.badlogic.gdx.ai.steer.utils.Path.createParam()"""
        pass

    @abstractmethod
    def getEndPoint(self, ):
        """public abstract T com.badlogic.gdx.ai.steer.utils.Path.getEndPoint()"""
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
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.utils.Path as __Path
__Path = __Path
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

 
class Path(ABC):
    """com.badlogic.gdx.ai.steer.utils.Path"""
 
    @staticmethod
    def __wrap(java_value: __Path) -> 'Path':
        return Path(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Path):
        """
        Dynamic initializer for Path.
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
    def createParam(self, ):
        """public abstract P com.badlogic.gdx.ai.steer.utils.Path.createParam()"""
        pass

    @abstractmethod
    def getEndPoint(self, ):
        """public abstract T com.badlogic.gdx.ai.steer.utils.Path.getEndPoint()"""
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
import com.badlogic.gdx.ai.steer.utils.Path as __Path_PathParam
__PathParam = __Path_PathParam.PathParam
from abc import abstractmethod, ABC
 
class PathParam(ABC):
    """com.badlogic.gdx.ai.steer.utils.Path.PathParam"""
 
    @staticmethod
    def __wrap(java_value: __PathParam) -> 'PathParam':
        return PathParam(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PathParam):
        """
        Dynamic initializer for PathParam.
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
    def setDistance(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.steer.utils.Path$PathParam.setDistance(float)"""
        pass

    @abstractmethod
    def getDistance(self, ):
        """public abstract float com.badlogic.gdx.ai.steer.utils.Path$PathParam.getDistance()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.RayConfiguration
import com.badlogic.gdx.ai.steer.utils.RayConfiguration as __RayConfiguration
__RayConfiguration = __RayConfiguration
from abc import abstractmethod, ABC
 
class RayConfiguration(ABC):
    """com.badlogic.gdx.ai.steer.utils.RayConfiguration"""
 
    @staticmethod
    def __wrap(java_value: __RayConfiguration) -> 'RayConfiguration':
        return RayConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RayConfiguration):
        """
        Dynamic initializer for RayConfiguration.
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
    def updateRays(self, ):
        """public abstract com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.RayConfiguration.updateRays()"""
        pass