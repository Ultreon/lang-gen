from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Ray():
    """com.badlogic.gdx.math.collision.Ray"""
 
    @staticmethod
    def _wrap(java_value: _Ray) -> 'Ray':
        return Ray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Ray):
        """
        Dynamic initializer for Ray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Ray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Ray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'Ray') -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.set(com.badlogic.gdx.math.collision.Ray)"""
        return 'Ray'._wrap(super(_Ray, self).set(arg0))

    @overload
    def cpy(self) -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.cpy()"""
        return 'Ray'._wrap(super(Ray, self).cpy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.set(float,float,float,float,float,float)"""
        return 'Ray'._wrap(super(_Ray, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.collision.Ray()"""
        val = _Ray()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mul(self, arg0: 'Matrix4') -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.mul(com.badlogic.gdx.math.Matrix4)"""
        return 'Ray'._wrap(super(_Ray, self).mul(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.collision.Ray.hashCode()"""
        return int._wrap(super(Ray, self).hashCode())

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public com.badlogic.gdx.math.collision.Ray(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = _Ray(arg0, arg1)
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.collision.Ray.equals(java.lang.Object)"""
        return bool._wrap(super(_Ray, self).equals(arg0))

    @overload
    def getEndPoint(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.Ray.getEndPoint(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_Ray, self).getEndPoint(arg0, _float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Ray'._wrap(super(_Ray, self).set(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.collision.Ray()"""
        val = _Ray()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.collision.Ray.toString()"""
        return str._wrap(super(Ray, self).toString())

 
 
 
# CLASS: com.badlogic.gdx.math.collision.Ray
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.math.collision.Ray as _Ray
_Ray = _Ray
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Ray():
    """com.badlogic.gdx.math.collision.Ray"""
 
    @staticmethod
    def _wrap(java_value: _Ray) -> 'Ray':
        return Ray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Ray):
        """
        Dynamic initializer for Ray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Ray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Ray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'Ray') -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.set(com.badlogic.gdx.math.collision.Ray)"""
        return 'Ray'._wrap(super(_Ray, self).set(arg0))

    @overload
    def cpy(self) -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.cpy()"""
        return 'Ray'._wrap(super(Ray, self).cpy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.set(float,float,float,float,float,float)"""
        return 'Ray'._wrap(super(_Ray, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.collision.Ray()"""
        val = _Ray()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mul(self, arg0: 'Matrix4') -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.mul(com.badlogic.gdx.math.Matrix4)"""
        return 'Ray'._wrap(super(_Ray, self).mul(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.collision.Ray.hashCode()"""
        return int._wrap(super(Ray, self).hashCode())

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public com.badlogic.gdx.math.collision.Ray(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = _Ray(arg0, arg1)
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.collision.Ray.equals(java.lang.Object)"""
        return bool._wrap(super(_Ray, self).equals(arg0))

    @overload
    def getEndPoint(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.Ray.getEndPoint(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_Ray, self).getEndPoint(arg0, _float.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Ray'._wrap(super(_Ray, self).set(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.collision.Ray()"""
        val = _Ray()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.collision.Ray.toString()"""
        return str._wrap(super(Ray, self).toString())

 
 
 
# CLASS: com.badlogic.gdx.math.collision.Ray 
 
 
# CLASS: com.badlogic.gdx.math.collision.OrientedBoundingBox
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.math.collision.OrientedBoundingBox as _OrientedBoundingBox
_OrientedBoundingBox = _OrientedBoundingBox
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OrientedBoundingBox():
    """com.badlogic.gdx.math.collision.OrientedBoundingBox"""
 
    @staticmethod
    def _wrap(java_value: _OrientedBoundingBox) -> 'OrientedBoundingBox':
        return OrientedBoundingBox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OrientedBoundingBox):
        """
        Dynamic initializer for OrientedBoundingBox.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OrientedBoundingBox__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OrientedBoundingBox__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'BoundingBox', arg1: 'Matrix4') -> 'OrientedBoundingBox':
        """public com.badlogic.gdx.math.collision.OrientedBoundingBox com.badlogic.gdx.math.collision.OrientedBoundingBox.set(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4)"""
        return 'OrientedBoundingBox'._wrap(super(_OrientedBoundingBox, self).set(arg0, arg1))

    @overload
    def getBounds(self) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.OrientedBoundingBox.getBounds()"""
        return 'BoundingBox'._wrap(super(OrientedBoundingBox, self).getBounds())

    @overload
    def getCorner101(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner101(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_OrientedBoundingBox, self).getCorner101(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.collision.OrientedBoundingBox.getTransform()"""
        return 'math.Matrix4'._wrap(super(OrientedBoundingBox, self).getTransform())

    @overload
    def intersects(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.OrientedBoundingBox.intersects(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool._wrap(super(_OrientedBoundingBox, self).intersects(arg0))

    @overload
    def getCorner111(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner111(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_OrientedBoundingBox, self).getCorner111(arg0))

    @overload
    def contains(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.collision.OrientedBoundingBox.contains(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_OrientedBoundingBox, self).contains(arg0))

    @overload
    def intersects(self, arg0: 'OrientedBoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.OrientedBoundingBox.intersects(com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool._wrap(super(_OrientedBoundingBox, self).intersects(arg0))

    @overload
    def getCorner010(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner010(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_OrientedBoundingBox, self).getCorner010(arg0))

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
    def getCorner100(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner100(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_OrientedBoundingBox, self).getCorner100(arg0))

    @overload
    def getCorner001(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner001(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_OrientedBoundingBox, self).getCorner001(arg0))

    @overload
    def getCorner000(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner000(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_OrientedBoundingBox, self).getCorner000(arg0))

    @overload
    def setBounds(self, arg0: 'BoundingBox'):
        """public void com.badlogic.gdx.math.collision.OrientedBoundingBox.setBounds(com.badlogic.gdx.math.collision.BoundingBox)"""
        super(_OrientedBoundingBox, self).setBounds(arg0)

    @overload
    def getCorner011(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner011(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_OrientedBoundingBox, self).getCorner011(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getCorner110(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner110(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_OrientedBoundingBox, self).getCorner110(arg0))

    @overload
    def contains(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.OrientedBoundingBox.contains(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool._wrap(super(_OrientedBoundingBox, self).contains(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'BoundingBox', arg1: 'Matrix4'):
        """public com.badlogic.gdx.math.collision.OrientedBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4)"""
        val = _OrientedBoundingBox(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'BoundingBox'):
        """public com.badlogic.gdx.math.collision.OrientedBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        val = _OrientedBoundingBox(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.collision.OrientedBoundingBox()"""
        val = _OrientedBoundingBox()
        self.__wrapper = val

    @overload
    def contains(self, arg0: 'OrientedBoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.OrientedBoundingBox.contains(com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool._wrap(super(_OrientedBoundingBox, self).contains(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.collision.OrientedBoundingBox()"""
        val = _OrientedBoundingBox()
        self.__wrapper = val

    @overload
    def getVertices(self) -> List['math.Vector3']:
        """public com.badlogic.gdx.math.Vector3[] com.badlogic.gdx.math.collision.OrientedBoundingBox.getVertices()"""
        return List['math.Vector3']._wrap(super(OrientedBoundingBox, self).getVertices())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.math.collision.OrientedBoundingBox.setTransform(com.badlogic.gdx.math.Matrix4)"""
        super(_OrientedBoundingBox, self).setTransform(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def mul(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.math.collision.OrientedBoundingBox.mul(com.badlogic.gdx.math.Matrix4)"""
        super(_OrientedBoundingBox, self).mul(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.collision.Segment
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
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.math.collision.Segment as _Segment
_Segment = _Segment
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Segment():
    """com.badlogic.gdx.math.collision.Segment"""
 
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
 
    @overload
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.collision.Segment.len2()"""
        return float._wrap(super(Segment, self).len2())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.collision.Segment.equals(java.lang.Object)"""
        return bool._wrap(super(_Segment, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public com.badlogic.gdx.math.collision.Segment(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = _Segment(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public com.badlogic.gdx.math.collision.Segment(float,float,float,float,float,float)"""
        val = _Segment(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))
        self.__wrapper = val

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

    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.collision.Segment.len()"""
        return float._wrap(super(Segment, self).len())

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
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.collision.Segment.hashCode()"""
        return int._wrap(super(Segment, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.math.collision.Sphere
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
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.math.collision.Sphere as _Sphere
_Sphere = _Sphere
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Sphere():
    """com.badlogic.gdx.math.collision.Sphere"""
 
    @staticmethod
    def _wrap(java_value: _Sphere) -> 'Sphere':
        return Sphere(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Sphere):
        """
        Dynamic initializer for Sphere.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Sphere__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Sphere__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def surfaceArea(self) -> float:
        """public float com.badlogic.gdx.math.collision.Sphere.surfaceArea()"""
        return float._wrap(super(Sphere, self).surfaceArea())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def volume(self) -> float:
        """public float com.badlogic.gdx.math.collision.Sphere.volume()"""
        return float._wrap(super(Sphere, self).volume())

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
    def overlaps(self, arg0: 'Sphere') -> bool:
        """public boolean com.badlogic.gdx.math.collision.Sphere.overlaps(com.badlogic.gdx.math.collision.Sphere)"""
        return bool._wrap(super(_Sphere, self).overlaps(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.collision.Sphere.hashCode()"""
        return int._wrap(super(Sphere, self).hashCode())

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
    def __init__(self, arg0: 'Vector3', arg1: float):
        """public com.badlogic.gdx.math.collision.Sphere(com.badlogic.gdx.math.Vector3,float)"""
        val = _Sphere(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.collision.Sphere.equals(java.lang.Object)"""
        return bool._wrap(super(_Sphere, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.collision.BoundingBox
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
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
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BoundingBox():
    """com.badlogic.gdx.math.collision.BoundingBox"""
 
    @staticmethod
    def _wrap(java_value: _BoundingBox) -> 'BoundingBox':
        return BoundingBox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BoundingBox):
        """
        Dynamic initializer for BoundingBox.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BoundingBox__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BoundingBox__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDepth(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getDepth()"""
        return float._wrap(super(BoundingBox, self).getDepth())

    @overload
    def getCorner110(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner110(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getCorner110(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.collision.BoundingBox()"""
        val = _BoundingBox()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.collision.BoundingBox()"""
        val = _BoundingBox()
        self.__wrapper = val

    @overload
    def getMin(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getMin(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getMin(arg0))

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
    def set(self, arg0: 'BoundingBox') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).set(arg0))

    @overload
    def getMax(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getMax(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getMax(arg0))

    @overload
    def intersects(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.intersects(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool._wrap(super(_BoundingBox, self).intersects(arg0))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getWidth()"""
        return float._wrap(super(BoundingBox, self).getWidth())

    @overload
    def contains(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.contains(com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_BoundingBox, self).contains(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getCorner001(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner001(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getCorner001(arg0))

    @overload
    def ext(self, arg0: 'Vector3', arg1: float) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.Vector3,float)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).ext(arg0, _float.valueOf(arg1)))

    @overload
    def getCorner010(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner010(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getCorner010(arg0))

    @overload
    def getCenter(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCenter(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getCenter(arg0))

    @overload
    def inf(self) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.inf()"""
        return 'BoundingBox'._wrap(super(BoundingBox, self).inf())

    @overload
    def getCorner011(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner011(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getCorner011(arg0))

    @overload
    def mul(self, arg0: 'Matrix4') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.mul(com.badlogic.gdx.math.Matrix4)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).mul(arg0))

    @overload
    def getCenterY(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getCenterY()"""
        return float._wrap(super(BoundingBox, self).getCenterY())

    @overload
    def ext(self, arg0: 'BoundingBox', arg1: 'Matrix4') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).ext(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public com.badlogic.gdx.math.collision.BoundingBox(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = _BoundingBox(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def getCorner101(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner101(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getCorner101(arg0))

    @overload
    def getCorner111(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner111(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getCorner111(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.collision.BoundingBox.toString()"""
        return str._wrap(super(BoundingBox, self).toString())

    @overload
    def set(self, arg0: 'List') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(java.util.List<com.badlogic.gdx.math.Vector3>)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).set(arg0))

    @overload
    def getDimensions(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getDimensions(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getDimensions(arg0))

    @overload
    def ext(self, arg0: float, arg1: float, arg2: float) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(float,float,float)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).ext(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).set(arg0, arg1))

    @overload
    def getCenterX(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getCenterX()"""
        return float._wrap(super(BoundingBox, self).getCenterX())

    @overload
    def isValid(self) -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.isValid()"""
        return bool._wrap(super(BoundingBox, self).isValid())

    @overload
    def ext(self, arg0: 'BoundingBox') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).ext(arg0))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getHeight()"""
        return float._wrap(super(BoundingBox, self).getHeight())

    @overload
    def getCorner000(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner000(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getCorner000(arg0))

    @overload
    def ext(self, arg0: 'Vector3') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.Vector3)"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).ext(arg0))

    @overload
    def set(self, arg0: 'Vector3') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(com.badlogic.gdx.math.Vector3[])"""
        return 'BoundingBox'._wrap(super(_BoundingBox, self).set(arg0))

    @overload
    def getCenterZ(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getCenterZ()"""
        return float._wrap(super(BoundingBox, self).getCenterZ())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def contains(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.contains(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool._wrap(super(_BoundingBox, self).contains(arg0))

    @overload
    def __init__(self, arg0: 'BoundingBox'):
        """public com.badlogic.gdx.math.collision.BoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        val = _BoundingBox(arg0)
        self.__wrapper = val

    @overload
    def contains(self, arg0: 'OrientedBoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.contains(com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool._wrap(super(_BoundingBox, self).contains(arg0))

    @overload
    def update(self):
        """public void com.badlogic.gdx.math.collision.BoundingBox.update()"""
        super(BoundingBox, self).update()

    @overload
    def getCorner100(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner100(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_BoundingBox, self).getCorner100(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def clr(self) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.clr()"""
        return 'BoundingBox'._wrap(super(BoundingBox, self).clr())