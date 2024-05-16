from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as _LinePath_LinePathParam
_LinePathParam = _LinePath_LinePathParam.LinePathParam
from builtins import str
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as _LinePath
_LinePath = _LinePath
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinePath():
    """com.badlogic.gdx.ai.steer.utils.paths.LinePath"""
 
    @staticmethod
    def _wrap(java_value: _LinePath) -> 'LinePath':
        return LinePath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinePath):
        """
        Dynamic initializer for LinePath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinePath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinePath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def calculateDistance(self, arg0: 'Vector', arg1: 'LinePathParam') -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculateDistance(T,com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam)"""
        return float._wrap(super(_LinePath, self).calculateDistance(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Array', arg1: bool):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath(com.badlogic.gdx.utils.Array<T>,boolean)"""
        val = _LinePath(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStartPoint(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath.getStartPoint()"""
        return 'math.Vector'._wrap(super(LinePath, self).getStartPoint())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath(com.badlogic.gdx.utils.Array<T>)"""
        val = _LinePath(arg0)
        self.__wrapper = val

    @override
    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.getLength()"""
        return float._wrap(super(LinePath, self).getLength())

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

    @override
    @overload
    def isOpen(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.utils.paths.LinePath.isOpen()"""
        return bool._wrap(super(LinePath, self).isOpen())

    @overload
    def calculatePointSegmentSquareDistance(self, arg0: 'Vector', arg1: 'Vector', arg2: 'Vector', arg3: 'Vector') -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculatePointSegmentSquareDistance(T,T,T,T)"""
        return float._wrap(super(_LinePath, self).calculatePointSegmentSquareDistance(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getSegments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment<T>> com.badlogic.gdx.ai.steer.utils.paths.LinePath.getSegments()"""
        return 'utils.Array'._wrap(super(LinePath, self).getSegments())

    @overload
    def calculateTargetPosition(self, arg0: 'Vector', arg1: 'LinePathParam', arg2: float):
        """public void com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculateTargetPosition(T,com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam,float)"""
        super(_LinePath, self).calculateTargetPosition(arg0, arg1, _float.valueOf(arg2))

    @overload
    def createPath(self, arg0: 'Array'):
        """public void com.badlogic.gdx.ai.steer.utils.paths.LinePath.createPath(com.badlogic.gdx.utils.Array<T>)"""
        super(_LinePath, self).createPath(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getEndPoint(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath.getEndPoint()"""
        return 'math.Vector'._wrap(super(LinePath, self).getEndPoint())

    @override
    @overload
    def createParam(self) -> 'LinePathParam':
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam com.badlogic.gdx.ai.steer.utils.paths.LinePath.createParam()"""
        return 'LinePathParam'._wrap(super(LinePath, self).createParam())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.paths.LinePath
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as _LinePath_LinePathParam
_LinePathParam = _LinePath_LinePathParam.LinePathParam
from builtins import str
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as _LinePath
_LinePath = _LinePath
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinePath():
    """com.badlogic.gdx.ai.steer.utils.paths.LinePath"""
 
    @staticmethod
    def _wrap(java_value: _LinePath) -> 'LinePath':
        return LinePath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinePath):
        """
        Dynamic initializer for LinePath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinePath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinePath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def calculateDistance(self, arg0: 'Vector', arg1: 'LinePathParam') -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculateDistance(T,com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam)"""
        return float._wrap(super(_LinePath, self).calculateDistance(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Array', arg1: bool):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath(com.badlogic.gdx.utils.Array<T>,boolean)"""
        val = _LinePath(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStartPoint(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath.getStartPoint()"""
        return 'math.Vector'._wrap(super(LinePath, self).getStartPoint())

    @overload
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath(com.badlogic.gdx.utils.Array<T>)"""
        val = _LinePath(arg0)
        self.__wrapper = val

    @override
    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.getLength()"""
        return float._wrap(super(LinePath, self).getLength())

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

    @override
    @overload
    def isOpen(self) -> bool:
        """public boolean com.badlogic.gdx.ai.steer.utils.paths.LinePath.isOpen()"""
        return bool._wrap(super(LinePath, self).isOpen())

    @overload
    def calculatePointSegmentSquareDistance(self, arg0: 'Vector', arg1: 'Vector', arg2: 'Vector', arg3: 'Vector') -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculatePointSegmentSquareDistance(T,T,T,T)"""
        return float._wrap(super(_LinePath, self).calculatePointSegmentSquareDistance(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getSegments(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment<T>> com.badlogic.gdx.ai.steer.utils.paths.LinePath.getSegments()"""
        return 'utils.Array'._wrap(super(LinePath, self).getSegments())

    @overload
    def calculateTargetPosition(self, arg0: 'Vector', arg1: 'LinePathParam', arg2: float):
        """public void com.badlogic.gdx.ai.steer.utils.paths.LinePath.calculateTargetPosition(T,com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam,float)"""
        super(_LinePath, self).calculateTargetPosition(arg0, arg1, _float.valueOf(arg2))

    @overload
    def createPath(self, arg0: 'Array'):
        """public void com.badlogic.gdx.ai.steer.utils.paths.LinePath.createPath(com.badlogic.gdx.utils.Array<T>)"""
        super(_LinePath, self).createPath(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getEndPoint(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath.getEndPoint()"""
        return 'math.Vector'._wrap(super(LinePath, self).getEndPoint())

    @override
    @overload
    def createParam(self) -> 'LinePathParam':
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam com.badlogic.gdx.ai.steer.utils.paths.LinePath.createParam()"""
        return 'LinePathParam'._wrap(super(LinePath, self).createParam())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.paths.LinePath 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as _LinePath_LinePathParam
_LinePathParam = _LinePath_LinePathParam.LinePathParam
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LinePathParam():
    """com.badlogic.gdx.ai.steer.utils.paths.LinePath.LinePathParam"""
 
    @staticmethod
    def _wrap(java_value: _LinePathParam) -> 'LinePathParam':
        return LinePathParam(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LinePathParam):
        """
        Dynamic initializer for LinePathParam.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LinePathParam__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LinePathParam__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam()"""
        val = _LinePathParam()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam()"""
        val = _LinePathParam()
        self.__wrapper = val

    @override
    @overload
    def setDistance(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam.setDistance(float)"""
        super(_LinePathParam, self).setDistance(_float.valueOf(arg0))

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

    @override
    @overload
    def getDistance(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam.getDistance()"""
        return float._wrap(super(LinePathParam, self).getDistance())

    @overload
    def getSegmentIndex(self) -> int:
        """public int com.badlogic.gdx.ai.steer.utils.paths.LinePath$LinePathParam.getSegmentIndex()"""
        return int._wrap(super(LinePathParam, self).getSegmentIndex())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.utils.paths.LinePath as _LinePath_Segment
_Segment = _LinePath_Segment.Segment
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.Vector as _Vector
_Vector = _Vector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Segment():
    """com.badlogic.gdx.ai.steer.utils.paths.LinePath.Segment"""
 
    @staticmethod
    def _wrap(java_value: _Segment) -> 'Segment':
        return Segment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Segment):
        """
        Dynamic initializer for Segment.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Segment__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Segment__wrapper":
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
    def getCumulativeLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment.getCumulativeLength()"""
        return float._wrap(super(Segment, self).getCumulativeLength())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getBegin(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment.getBegin()"""
        return 'math.Vector'._wrap(super(Segment, self).getBegin())

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
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment.getLength()"""
        return float._wrap(super(Segment, self).getLength())

    @overload
    def getEnd(self) -> 'math.Vector':
        """public T com.badlogic.gdx.ai.steer.utils.paths.LinePath$Segment.getEnd()"""
        return 'math.Vector'._wrap(super(Segment, self).getEnd())

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