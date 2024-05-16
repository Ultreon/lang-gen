from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator as _DistanceFieldGenerator
_DistanceFieldGenerator = _DistanceFieldGenerator
from builtins import float
import java.awt.image.BufferedImage as _BufferedImage
_BufferedImage = _BufferedImage
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DistanceFieldGenerator():
    """com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator"""
 
    @staticmethod
    def _wrap(java_value: _DistanceFieldGenerator) -> 'DistanceFieldGenerator':
        return DistanceFieldGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DistanceFieldGenerator):
        """
        Dynamic initializer for DistanceFieldGenerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DistanceFieldGenerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DistanceFieldGenerator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator()"""
        val = _DistanceFieldGenerator()
        self.__wrapper = val

    @overload
    def generateDistanceField(self, arg0: 'BufferedImage') -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.generateDistanceField(java.awt.image.BufferedImage)"""
        return 'BufferedImage'._wrap(super(_DistanceFieldGenerator, self).generateDistanceField(arg0))

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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setColor(java.awt.Color)"""
        super(_DistanceFieldGenerator, self).setColor(arg0)

    @overload
    def getSpread(self) -> float:
        """public float com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getSpread()"""
        return float._wrap(super(DistanceFieldGenerator, self).getSpread())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.main(java.lang.String[])"""
        _DistanceFieldGenerator.main(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getDownscale(self) -> int:
        """public int com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getDownscale()"""
        return int._wrap(super(DistanceFieldGenerator, self).getDownscale())

    @overload
    def setSpread(self, arg0: float):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setSpread(float)"""
        super(_DistanceFieldGenerator, self).setSpread(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setDownscale(self, arg0: int):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setDownscale(int)"""
        super(_DistanceFieldGenerator, self).setDownscale(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator()"""
        val = _DistanceFieldGenerator()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getColor()"""
        return 'Color'._wrap(super(DistanceFieldGenerator, self).getColor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator as _DistanceFieldGenerator
_DistanceFieldGenerator = _DistanceFieldGenerator
from builtins import float
import java.awt.image.BufferedImage as _BufferedImage
_BufferedImage = _BufferedImage
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DistanceFieldGenerator():
    """com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator"""
 
    @staticmethod
    def _wrap(java_value: _DistanceFieldGenerator) -> 'DistanceFieldGenerator':
        return DistanceFieldGenerator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DistanceFieldGenerator):
        """
        Dynamic initializer for DistanceFieldGenerator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DistanceFieldGenerator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DistanceFieldGenerator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator()"""
        val = _DistanceFieldGenerator()
        self.__wrapper = val

    @overload
    def generateDistanceField(self, arg0: 'BufferedImage') -> 'BufferedImage':
        """public java.awt.image.BufferedImage com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.generateDistanceField(java.awt.image.BufferedImage)"""
        return 'BufferedImage'._wrap(super(_DistanceFieldGenerator, self).generateDistanceField(arg0))

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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setColor(java.awt.Color)"""
        super(_DistanceFieldGenerator, self).setColor(arg0)

    @overload
    def getSpread(self) -> float:
        """public float com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getSpread()"""
        return float._wrap(super(DistanceFieldGenerator, self).getSpread())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.main(java.lang.String[])"""
        _DistanceFieldGenerator.main(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getDownscale(self) -> int:
        """public int com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getDownscale()"""
        return int._wrap(super(DistanceFieldGenerator, self).getDownscale())

    @overload
    def setSpread(self, arg0: float):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setSpread(float)"""
        super(_DistanceFieldGenerator, self).setSpread(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setDownscale(self, arg0: int):
        """public void com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.setDownscale(int)"""
        super(_DistanceFieldGenerator, self).setDownscale(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator()"""
        val = _DistanceFieldGenerator()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator.getColor()"""
        return 'Color'._wrap(super(DistanceFieldGenerator, self).getColor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.tools.distancefield.DistanceFieldGenerator