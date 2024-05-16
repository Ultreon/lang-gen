from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as __LinePath_LinePathParam
__LinePathParam = __LinePath_LinePathParam.LinePathParam
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as __LinePath
__LinePath = __LinePath
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import int
 
class LinePath():
    """com.badlogic.gdx.ai.steer.utils.paths.LinePath"""
 
    @staticmethod
    def __wrap(java_value: __LinePath) -> 'LinePath':
        return LinePath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinePath):
        """
        Dynamic initializer for LinePath.
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
    def calculateDistance(self, arg0: 'Vector', arg1: 'LinePathParam') -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculateDistance(T,com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam)"""
        return float.__wrap(super(__LinePath, self).calculateDistance(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def createPath(self, arg0: 'Array'):
        """public void com.badlogic.gdx.ai.steer.utils.paths.LinePath.createPath(com.badlogic.gdx.utils.Array<T>)"""
        super(__LinePath, self).createPath(arg0)

    @override
    @overload
    def createParam(self) -> 'LinePathParam':
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam com.badlogic.gdx.ai.steer.utils.paths.LinePath.createParam()"""
        return 'LinePathParam'.__wrap(super(LinePath, self).createParam())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getStartPoint(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath.getStartPoint()"""
        return 'math.Vector'.__wrap(super(LinePath, self).getStartPoint())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSegments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment<T>> com.badlogic.gdx.ai.steer.utils.paths.LinePath.getSegments()"""
        return 'utils.Array'.__wrap(super(LinePath, self).getSegments())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Array', arg1: bool):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath(com.badlogic.gdx.utils.Array<T>,boolean)"""
        val = __LinePath(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def calculatePointSegmentSquareDistance(self, arg0: 'Vector', arg1: 'Vector', arg2: 'Vector', arg3: 'Vector') -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculatePointSegmentSquareDistance(T,T,T,T)"""
        return float.__wrap(super(__LinePath, self).calculatePointSegmentSquareDistance(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isOpen(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.utils.paths.LinePath.isOpen()"""
        return bool.__wrap(super(LinePath, self).isOpen())

    @override
    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.getLength()"""
        return float.__wrap(super(LinePath, self).getLength())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath(com.badlogic.gdx.utils.Array<T>)"""
        val = __LinePath(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def calculateTargetPosition(self, arg0: 'Vector', arg1: 'LinePathParam', arg2: float):
        """public void com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculateTargetPosition(T,com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam,float)"""
        super(__LinePath, self).calculateTargetPosition(arg0, arg1, __float.valueOf(arg2))

    @override
    @overload
    def getEndPoint(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath.getEndPoint()"""
        return 'math.Vector'.__wrap(super(LinePath, self).getEndPoint())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.paths.LinePath
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as __LinePath_LinePathParam
__LinePathParam = __LinePath_LinePathParam.LinePathParam
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as __LinePath
__LinePath = __LinePath
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import int
 
class LinePath():
    """com.badlogic.gdx.ai.steer.utils.paths.LinePath"""
 
    @staticmethod
    def __wrap(java_value: __LinePath) -> 'LinePath':
        return LinePath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinePath):
        """
        Dynamic initializer for LinePath.
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
    def calculateDistance(self, arg0: 'Vector', arg1: 'LinePathParam') -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculateDistance(T,com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam)"""
        return float.__wrap(super(__LinePath, self).calculateDistance(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def createPath(self, arg0: 'Array'):
        """public void com.badlogic.gdx.ai.steer.utils.paths.LinePath.createPath(com.badlogic.gdx.utils.Array<T>)"""
        super(__LinePath, self).createPath(arg0)

    @override
    @overload
    def createParam(self) -> 'LinePathParam':
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam com.badlogic.gdx.ai.steer.utils.paths.LinePath.createParam()"""
        return 'LinePathParam'.__wrap(super(LinePath, self).createParam())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getStartPoint(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath.getStartPoint()"""
        return 'math.Vector'.__wrap(super(LinePath, self).getStartPoint())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSegments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment<T>> com.badlogic.gdx.ai.steer.utils.paths.LinePath.getSegments()"""
        return 'utils.Array'.__wrap(super(LinePath, self).getSegments())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Array', arg1: bool):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath(com.badlogic.gdx.utils.Array<T>,boolean)"""
        val = __LinePath(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def calculatePointSegmentSquareDistance(self, arg0: 'Vector', arg1: 'Vector', arg2: 'Vector', arg3: 'Vector') -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculatePointSegmentSquareDistance(T,T,T,T)"""
        return float.__wrap(super(__LinePath, self).calculatePointSegmentSquareDistance(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isOpen(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.utils.paths.LinePath.isOpen()"""
        return bool.__wrap(super(LinePath, self).isOpen())

    @override
    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.getLength()"""
        return float.__wrap(super(LinePath, self).getLength())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath(com.badlogic.gdx.utils.Array<T>)"""
        val = __LinePath(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def calculateTargetPosition(self, arg0: 'Vector', arg1: 'LinePathParam', arg2: float):
        """public void com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculateTargetPosition(T,com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam,float)"""
        super(__LinePath, self).calculateTargetPosition(arg0, arg1, __float.valueOf(arg2))

    @override
    @overload
    def getEndPoint(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath.getEndPoint()"""
        return 'math.Vector'.__wrap(super(LinePath, self).getEndPoint())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.paths.LinePath 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as __LinePath_Segment
__Segment = __LinePath_Segment.Segment
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
import com.badlogic.gdx.math.Vector as __Vector
__Vector = __Vector
from builtins import bool
from builtins import int
 
class Segment():
    """com.badlogic.gdx.ai.steer.utils.paths.LinePath.Segment"""
 
    @staticmethod
    def __wrap(java_value: __Segment) -> 'Segment':
        return Segment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Segment):
        """
        Dynamic initializer for Segment.
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
    def getCumulativeLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment.getCumulativeLength()"""
        return float.__wrap(super(Segment, self).getCumulativeLength())

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
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment.getLength()"""
        return float.__wrap(super(Segment, self).getLength())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getEnd(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment.getEnd()"""
        return 'math.Vector'.__wrap(super(Segment, self).getEnd())

    @overload
    def getBegin(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment.getBegin()"""
        return 'math.Vector'.__wrap(super(Segment, self).getBegin())

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
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as __LinePath_LinePathParam
__LinePathParam = __LinePath_LinePathParam.LinePathParam
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
 
class LinePathParam():
    """com.badlogic.gdx.ai.steer.utils.paths.LinePath.LinePathParam"""
 
    @staticmethod
    def __wrap(java_value: __LinePathParam) -> 'LinePathParam':
        return LinePathParam(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LinePathParam):
        """
        Dynamic initializer for LinePathParam.
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
    def __init__(self):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam()"""
        val = __LinePathParam()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getDistance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam.getDistance()"""
        return float.__wrap(super(LinePathParam, self).getDistance())

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
    def setDistance(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam.setDistance(float)"""
        super(__LinePathParam, self).setDistance(__float.valueOf(arg0))

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
    def getSegmentIndex(self) -> int:
        """public int com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam.getSegmentIndex()"""
        return int.__wrap(super(LinePathParam, self).getSegmentIndex())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam()"""
        val = __LinePathParam()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))