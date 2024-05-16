from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.awt.Stroke as Stroke
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect as __OutlineEffect
__OutlineEffect = __OutlineEffect
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

import java.awt.Stroke as __Stroke
__Stroke = __Stroke
import java.awt.Color as __Color
__Color = __Color
import java.util.List as __List
__List = __List
import java.awt.Graphics2D as Graphics2D
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect as __OutlineWobbleEffect
__OutlineWobbleEffect = __OutlineWobbleEffect
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class OutlineWobbleEffect(__OutlineEffect, OutlineEffect):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect"""
 
    @staticmethod
    def __wrap(java_value: __OutlineWobbleEffect) -> 'OutlineWobbleEffect':
        return OutlineWobbleEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OutlineWobbleEffect):
        """
        Dynamic initializer for OutlineWobbleEffect.
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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setColor(java.awt.Color)"""
        super(__OutlineEffect, self).setColor(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getJoin(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getJoin()"""
        return int.__wrap(super(OutlineEffect, self).getJoin())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect()"""
        val = __OutlineWobbleEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(__OutlineEffect, self).draw(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect()"""
        val = __OutlineWobbleEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect.setValues(java.util.List)"""
        super(__OutlineWobbleEffect, self).setValues(arg0)

    @override
    @overload
    def setWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setWidth(int)"""
        super(__OutlineEffect, self).setWidth(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect.toString()"""
        return str.__wrap(super(OutlineWobbleEffect, self).toString())

    @override
    @overload
    def getStroke(self) -> 'Stroke':
        """public java.awt.Stroke com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getStroke()"""
        return 'Stroke'.__wrap(super(OutlineEffect, self).getStroke())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setStroke(self, arg0: 'Stroke'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setStroke(java.awt.Stroke)"""
        super(__OutlineEffect, self).setStroke(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getWidth()"""
        return float.__wrap(super(OutlineEffect, self).getWidth())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setJoin(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setJoin(int)"""
        super(__OutlineEffect, self).setJoin(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'Color'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect(int,java.awt.Color)"""
        val = __OutlineWobbleEffect(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect.getValues()"""
        return 'List'.__wrap(super(OutlineWobbleEffect, self).getValues())

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

    @override
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getColor()"""
        return 'Color'.__wrap(super(OutlineEffect, self).getColor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.awt.Stroke as Stroke
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect as __OutlineEffect
__OutlineEffect = __OutlineEffect
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

import java.awt.Stroke as __Stroke
__Stroke = __Stroke
import java.awt.Color as __Color
__Color = __Color
import java.util.List as __List
__List = __List
import java.awt.Graphics2D as Graphics2D
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect as __OutlineWobbleEffect
__OutlineWobbleEffect = __OutlineWobbleEffect
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class OutlineWobbleEffect(__OutlineEffect, OutlineEffect):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect"""
 
    @staticmethod
    def __wrap(java_value: __OutlineWobbleEffect) -> 'OutlineWobbleEffect':
        return OutlineWobbleEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OutlineWobbleEffect):
        """
        Dynamic initializer for OutlineWobbleEffect.
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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setColor(java.awt.Color)"""
        super(__OutlineEffect, self).setColor(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getJoin(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getJoin()"""
        return int.__wrap(super(OutlineEffect, self).getJoin())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect()"""
        val = __OutlineWobbleEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(__OutlineEffect, self).draw(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect()"""
        val = __OutlineWobbleEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect.setValues(java.util.List)"""
        super(__OutlineWobbleEffect, self).setValues(arg0)

    @override
    @overload
    def setWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setWidth(int)"""
        super(__OutlineEffect, self).setWidth(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect.toString()"""
        return str.__wrap(super(OutlineWobbleEffect, self).toString())

    @override
    @overload
    def getStroke(self) -> 'Stroke':
        """public java.awt.Stroke com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getStroke()"""
        return 'Stroke'.__wrap(super(OutlineEffect, self).getStroke())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setStroke(self, arg0: 'Stroke'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setStroke(java.awt.Stroke)"""
        super(__OutlineEffect, self).setStroke(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getWidth()"""
        return float.__wrap(super(OutlineEffect, self).getWidth())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setJoin(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setJoin(int)"""
        super(__OutlineEffect, self).setJoin(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'Color'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect(int,java.awt.Color)"""
        val = __OutlineWobbleEffect(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect.getValues()"""
        return 'List'.__wrap(super(OutlineWobbleEffect, self).getValues())

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

    @override
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getColor()"""
        return 'Color'.__wrap(super(OutlineEffect, self).getColor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.awt.Stroke as Stroke
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect as __OutlineEffect
__OutlineEffect = __OutlineEffect
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

import java.awt.Stroke as __Stroke
__Stroke = __Stroke
import java.awt.Color as __Color
__Color = __Color
import java.util.List as __List
__List = __List
import java.awt.Graphics2D as Graphics2D
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class OutlineEffect(__ConfigurableEffect, ConfigurableEffect):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect"""
 
    @staticmethod
    def __wrap(java_value: __OutlineEffect) -> 'OutlineEffect':
        return OutlineEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OutlineEffect):
        """
        Dynamic initializer for OutlineEffect.
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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setColor(java.awt.Color)"""
        super(__OutlineEffect, self).setColor(arg0)

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getValues()"""
        return 'List'.__wrap(super(OutlineEffect, self).getValues())

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(__OutlineEffect, self).draw(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, arg0: int, arg1: 'Color'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect(int,java.awt.Color)"""
        val = __OutlineEffect(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getColor()"""
        return 'Color'.__wrap(super(OutlineEffect, self).getColor())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getJoin(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getJoin()"""
        return int.__wrap(super(OutlineEffect, self).getJoin())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.toString()"""
        return str.__wrap(super(OutlineEffect, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect()"""
        val = __OutlineEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setWidth(int)"""
        super(__OutlineEffect, self).setWidth(__int.valueOf(arg0))

    @overload
    def getStroke(self) -> 'Stroke':
        """public java.awt.Stroke com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getStroke()"""
        return 'Stroke'.__wrap(super(OutlineEffect, self).getStroke())

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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect()"""
        val = __OutlineEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getWidth()"""
        return float.__wrap(super(OutlineEffect, self).getWidth())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setValues(java.util.List)"""
        super(__OutlineEffect, self).setValues(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setJoin(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setJoin(int)"""
        super(__OutlineEffect, self).setJoin(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setStroke(self, arg0: 'Stroke'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setStroke(java.awt.Stroke)"""
        super(__OutlineEffect, self).setStroke(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect as __GradientEffect
__GradientEffect = __GradientEffect
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

import java.awt.Color as __Color
__Color = __Color
import java.util.List as __List
__List = __List
import java.awt.Graphics2D as Graphics2D
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class GradientEffect(__ConfigurableEffect, ConfigurableEffect):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect"""
 
    @staticmethod
    def __wrap(java_value: __GradientEffect) -> 'GradientEffect':
        return GradientEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GradientEffect):
        """
        Dynamic initializer for GradientEffect.
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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect()"""
        val = __GradientEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setTopColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setTopColor(java.awt.Color)"""
        super(__GradientEffect, self).setTopColor(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCyclic(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setCyclic(boolean)"""
        super(__GradientEffect, self).setCyclic(__boolean.valueOf(arg0))

    @overload
    def getScale(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.getScale()"""
        return float.__wrap(super(GradientEffect, self).getScale())

    @overload
    def getOffset(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.getOffset()"""
        return int.__wrap(super(GradientEffect, self).getOffset())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getBottomColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.getBottomColor()"""
        return 'Color'.__wrap(super(GradientEffect, self).getBottomColor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Color', arg1: 'Color', arg2: float):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect(java.awt.Color,java.awt.Color,float)"""
        val = __GradientEffect(arg0, arg1, __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.getValues()"""
        return 'List'.__wrap(super(GradientEffect, self).getValues())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.toString()"""
        return str.__wrap(super(GradientEffect, self).toString())

    @overload
    def setOffset(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setOffset(int)"""
        super(__GradientEffect, self).setOffset(__int.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(__GradientEffect, self).draw(arg0, arg1, arg2, arg3)

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setScale(float)"""
        super(__GradientEffect, self).setScale(__float.valueOf(arg0))

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
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect()"""
        val = __GradientEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setBottomColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setBottomColor(java.awt.Color)"""
        super(__GradientEffect, self).setBottomColor(arg0)

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setValues(java.util.List)"""
        super(__GradientEffect, self).setValues(arg0)

    @overload
    def isCyclic(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.isCyclic()"""
        return bool.__wrap(super(GradientEffect, self).isCyclic())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTopColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.getTopColor()"""
        return 'Color'.__wrap(super(GradientEffect, self).getTopColor()) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

import java.util.List as __List
__List = __List
import java.awt.Graphics2D as Graphics2D
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect as __DistanceFieldEffect
__DistanceFieldEffect = __DistanceFieldEffect
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class DistanceFieldEffect(__ConfigurableEffect, ConfigurableEffect):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect"""
 
    @staticmethod
    def __wrap(java_value: __DistanceFieldEffect) -> 'DistanceFieldEffect':
        return DistanceFieldEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DistanceFieldEffect):
        """
        Dynamic initializer for DistanceFieldEffect.
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

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect.setValues(java.util.List)"""
        super(__DistanceFieldEffect, self).setValues(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(__DistanceFieldEffect, self).draw(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect()"""
        val = __DistanceFieldEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect()"""
        val = __DistanceFieldEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect.toString()"""
        return str.__wrap(super(DistanceFieldEffect, self).toString())

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

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect.getValues()"""
        return 'List'.__wrap(super(DistanceFieldEffect, self).getValues())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.awt.image.BufferedImageOp as __BufferedImageOp
__BufferedImageOp = __BufferedImageOp
from builtins import type
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

import java.awt.Graphics2D as Graphics2D
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect as __FilterEffect
__FilterEffect = __FilterEffect
import java.awt.image.BufferedImageOp as BufferedImageOp
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FilterEffect(__Effect, Effect):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect"""
 
    @staticmethod
    def __wrap(java_value: __FilterEffect) -> 'FilterEffect':
        return FilterEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FilterEffect):
        """
        Dynamic initializer for FilterEffect.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getFilter(self) -> 'BufferedImageOp':
        """public java.awt.image.BufferedImageOp com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect.getFilter()"""
        return 'BufferedImageOp'.__wrap(super(FilterEffect, self).getFilter())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setFilter(self, arg0: 'BufferedImageOp'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect.setFilter(java.awt.image.BufferedImageOp)"""
        super(__FilterEffect, self).setFilter(arg0)

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def __init__(self, arg0: 'BufferedImageOp'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect(java.awt.image.BufferedImageOp)"""
        val = __FilterEffect(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(__FilterEffect, self).draw(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect()"""
        val = __FilterEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect()"""
        val = __FilterEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.awt.Stroke as Stroke
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect as __OutlineEffect
__OutlineEffect = __OutlineEffect
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

import java.awt.Stroke as __Stroke
__Stroke = __Stroke
import java.awt.Color as __Color
__Color = __Color
import java.util.List as __List
__List = __List
import java.awt.Graphics2D as Graphics2D
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect as __OutlineZigzagEffect
__OutlineZigzagEffect = __OutlineZigzagEffect
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class OutlineZigzagEffect(__OutlineEffect, OutlineEffect):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect"""
 
    @staticmethod
    def __wrap(java_value: __OutlineZigzagEffect) -> 'OutlineZigzagEffect':
        return OutlineZigzagEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OutlineZigzagEffect):
        """
        Dynamic initializer for OutlineZigzagEffect.
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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setColor(java.awt.Color)"""
        super(__OutlineEffect, self).setColor(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: 'Color'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect(int,java.awt.Color)"""
        val = __OutlineZigzagEffect(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getJoin(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getJoin()"""
        return int.__wrap(super(OutlineEffect, self).getJoin())

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect.getValues()"""
        return 'List'.__wrap(super(OutlineZigzagEffect, self).getValues())

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(__OutlineEffect, self).draw(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setWidth(int)"""
        super(__OutlineEffect, self).setWidth(__int.valueOf(arg0))

    @override
    @overload
    def getStroke(self) -> 'Stroke':
        """public java.awt.Stroke com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getStroke()"""
        return 'Stroke'.__wrap(super(OutlineEffect, self).getStroke())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect.toString()"""
        return str.__wrap(super(OutlineZigzagEffect, self).toString())

    @override
    @overload
    def setStroke(self, arg0: 'Stroke'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setStroke(java.awt.Stroke)"""
        super(__OutlineEffect, self).setStroke(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect()"""
        val = __OutlineZigzagEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getWidth()"""
        return float.__wrap(super(OutlineEffect, self).getWidth())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setJoin(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setJoin(int)"""
        super(__OutlineEffect, self).setJoin(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect()"""
        val = __OutlineZigzagEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect.setValues(java.util.List)"""
        super(__OutlineZigzagEffect, self).setValues(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getColor()"""
        return 'Color'.__wrap(super(OutlineEffect, self).getColor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

import java.awt.Color as __Color
__Color = __Color
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect as __ColorEffect
__ColorEffect = __ColorEffect
import java.util.List as __List
__List = __List
import java.awt.Graphics2D as Graphics2D
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class ColorEffect(__ConfigurableEffect, ConfigurableEffect):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect"""
 
    @staticmethod
    def __wrap(java_value: __ColorEffect) -> 'ColorEffect':
        return ColorEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ColorEffect):
        """
        Dynamic initializer for ColorEffect.
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
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.getColor()"""
        return 'Color'.__wrap(super(ColorEffect, self).getColor())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.setColor(java.awt.Color)"""
        super(__ColorEffect, self).setColor(arg0)

    @overload
    def __init__(self, arg0: 'Color'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect(java.awt.Color)"""
        val = __ColorEffect(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.toString()"""
        return str.__wrap(super(ColorEffect, self).toString())

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
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.setValues(java.util.List)"""
        super(__ColorEffect, self).setValues(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect()"""
        val = __ColorEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect()"""
        val = __ColorEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(__ColorEffect, self).draw(arg0, arg1, arg2, arg3)

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

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.getValues()"""
        return 'List'.__wrap(super(ColorEffect, self).getValues())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect
from pyquantum_helper import import_once as __import_once__
import java.awt.Graphics2D as Graphics2D
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect as __ConfigurableEffect
__ConfigurableEffect = __ConfigurableEffect
import java.awt.image.BufferedImage as BufferedImage
from abc import abstractmethod, ABC
import com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect as __Effect
__Effect = __Effect
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

import java.util.List as List
 
class ConfigurableEffect(ABC, __Effect, Effect):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect"""
 
    @staticmethod
    def __wrap(java_value: __ConfigurableEffect) -> 'ConfigurableEffect':
        return ConfigurableEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConfigurableEffect):
        """
        Dynamic initializer for ConfigurableEffect.
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
    def setValues(self, arg0: 'List'):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect.setValues(java.util.List)"""
        pass

    @abstractmethod
    def getValues(self, ):
        """public abstract java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect.getValues()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect as __ConfigurableEffect_Value
__Value = __ConfigurableEffect_Value.Value
from abc import abstractmethod, ABC
 
class Value(ABC):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect.Value"""
 
    @staticmethod
    def __wrap(java_value: __Value) -> 'Value':
        return Value(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Value):
        """
        Dynamic initializer for Value.
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
    def getObject(self, ):
        """public abstract java.lang.Object com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value.getObject()"""
        pass

    @abstractmethod
    def getString(self, ):
        """public abstract java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value.getString()"""
        pass

    @abstractmethod
    def setString(self, arg0: str):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value.setString(java.lang.String)"""
        pass

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value.getName()"""
        pass

    @abstractmethod
    def showDialog(self, ):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value.showDialog()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.awt.image.BufferedImage as __BufferedImage
__BufferedImage = __BufferedImage
import java.awt.Color as __Color
__Color = __Color
import com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil as __EffectUtil
__EffectUtil = __EffectUtil
import java.lang.Long as __long
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect as __ConfigurableEffect_Value
__Value = __ConfigurableEffect_Value.Value
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EffectUtil():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil"""
 
    @staticmethod
    def __wrap(java_value: __EffectUtil) -> 'EffectUtil':
        return EffectUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EffectUtil):
        """
        Dynamic initializer for EffectUtil.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def colorValue(arg0: str, arg1: 'Color') -> 'Value':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.colorValue(java.lang.String,java.awt.Color)"""
        return Value.__wrap(__EffectUtil.colorValue(arg0, arg1))

    @staticmethod
    @overload
    def getScratchImage() -> 'BufferedImage':
        """public static java.awt.image.BufferedImage com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.getScratchImage()"""
        return BufferedImage.__wrap(__EffectUtil.getScratchImage())

    @staticmethod
    @overload
    def floatValue(arg0: str, arg1: float, arg2: float, arg3: float, arg4: str) -> 'Value':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.floatValue(java.lang.String,float,float,float,java.lang.String)"""
        return Value.__wrap(__EffectUtil.floatValue(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def fromString(arg0: str) -> 'Color':
        """public static java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.fromString(java.lang.String)"""
        return Color.__wrap(__EffectUtil.fromString(arg0))

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

    @staticmethod
    @overload
    def optionValue(arg0: str, arg1: str, arg2: 'String', arg3: str) -> 'Value':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.optionValue(java.lang.String,java.lang.String,java.lang.String[][],java.lang.String)"""
        return Value.__wrap(__EffectUtil.optionValue(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def booleanValue(arg0: str, arg1: bool, arg2: str) -> 'Value':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.booleanValue(java.lang.String,boolean,java.lang.String)"""
        return Value.__wrap(__EffectUtil.booleanValue(arg0, __boolean.valueOf(arg1), arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def intValue(arg0: str, arg1: int, arg2: str) -> 'Value':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.intValue(java.lang.String,int,java.lang.String)"""
        return Value.__wrap(__EffectUtil.intValue(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil()"""
        val = __EffectUtil()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def toString(arg0: 'Color') -> str:
        """public static java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.toString(java.awt.Color)"""
        return str.__wrap(__EffectUtil.toString(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil()"""
        val = __EffectUtil()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect as __ShadowEffect
__ShadowEffect = __ShadowEffect
from builtins import float
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

import java.awt.Color as __Color
__Color = __Color
import java.util.List as __List
__List = __List
import java.awt.Graphics2D as Graphics2D
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import java.lang.Object as __Object
__Object = __Object
import java.awt.image.BufferedImage as BufferedImage
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class ShadowEffect(__ConfigurableEffect, ConfigurableEffect):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect"""
 
    @staticmethod
    def __wrap(java_value: __ShadowEffect) -> 'ShadowEffect':
        return ShadowEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShadowEffect):
        """
        Dynamic initializer for ShadowEffect.
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
    def setXDistance(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setXDistance(float)"""
        super(__ShadowEffect, self).setXDistance(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getValues()"""
        return 'List'.__wrap(super(ShadowEffect, self).getValues())

    @overload
    def __init__(self, arg0: 'Color', arg1: int, arg2: int, arg3: float):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect(java.awt.Color,int,int,float)"""
        val = __ShadowEffect(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(__ShadowEffect, self).draw(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect()"""
        val = __ShadowEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect()"""
        val = __ShadowEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getXDistance(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getXDistance()"""
        return float.__wrap(super(ShadowEffect, self).getXDistance())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setYDistance(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setYDistance(float)"""
        super(__ShadowEffect, self).setYDistance(__float.valueOf(arg0))

    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setOpacity(float)"""
        super(__ShadowEffect, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getBlurKernelSize(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getBlurKernelSize()"""
        return int.__wrap(super(ShadowEffect, self).getBlurKernelSize())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setValues(java.util.List)"""
        super(__ShadowEffect, self).setValues(arg0)

    @overload
    def setBlurKernelSize(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setBlurKernelSize(int)"""
        super(__ShadowEffect, self).setBlurKernelSize(__int.valueOf(arg0))

    @overload
    def getBlurPasses(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getBlurPasses()"""
        return int.__wrap(super(ShadowEffect, self).getBlurPasses())

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
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getOpacity()"""
        return float.__wrap(super(ShadowEffect, self).getOpacity())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.toString()"""
        return str.__wrap(super(ShadowEffect, self).toString())

    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getColor()"""
        return 'Color'.__wrap(super(ShadowEffect, self).getColor())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setColor(java.awt.Color)"""
        super(__ShadowEffect, self).setColor(arg0)

    @overload
    def getYDistance(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getYDistance()"""
        return float.__wrap(super(ShadowEffect, self).getYDistance())

    @overload
    def setBlurPasses(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setBlurPasses(int)"""
        super(__ShadowEffect, self).setBlurPasses(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect
from pyquantum_helper import import_once as __import_once__
import java.awt.Graphics2D as Graphics2D
import java.awt.image.BufferedImage as BufferedImage
import com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect as __Effect
__Effect = __Effect
from abc import abstractmethod, ABC
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

 
class Effect(ABC):
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect"""
 
    @staticmethod
    def __wrap(java_value: __Effect) -> 'Effect':
        return Effect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Effect):
        """
        Dynamic initializer for Effect.
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
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        pass