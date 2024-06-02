function $DYNAMIC_INIT$_$ImportName$($dynamic$) {
    // STUB
    return undefined
}

class Java {
    static type(name) {
        return name
    }

    static extend(name) {
        return name
    }
}

class $JavaBoxedType$ {
    $JavaPrimitiveType$Value() {
        return this
    }

    static valueOf(value) {
        return value
    }
}

class Symbol {
    toString() {
        return this
    }

    static iterator() {
        return this
    }
}

class Iterable {
    [Symbol.iterator]() {
        return this
    }

    forEach(func) {
        // STUB
    }
}

class Object {
    static keys() {
        return new Iterable()
    }
}

//:::TEMPLATE_START{"id":"imports","properties":["ImportName","ImportAsName","ImportPath"]}
import {$ImportName$ as $ImportAsName$} from "$ImportPath$/$ImportName$.mjs"
//:::TEMPLATE_END

//:::TEMPLATE_START{"id":"java_imports","properties":["ImportName","ImportPath","ImportPackage","TemplateJavaClassName"]}
const _$TemplateJavaClassName$ = Java.type("$ImportPackage$.$ImportName$");
//:::TEMPLATE_END

//:::TEMPLATE_START{"id":"class","properties":["Imports","JavaImports","TemplateClassName","TemplateJavaClassName","Parents","JavaConstants","StaticMethods","Properties","Methods"]}
//$Imports$//
//$JavaImports$//

const DYNAMIC_INIT = {};

export function $DYNAMIC_INIT$_$TemplateClassName$($dynamic$) {
    return new $TemplateClassName$(DYNAMIC_INIT, $dynamic$);
}

/**
 * AUTO GENERATED CODE - DO NOT EDIT
 * Class for {_$TemplateClassName$}
 */
export class $TemplateClassName$ {
    $JavaConstants$

    $dynamic$

    constructor(...args) {
        if (args.length === 2 && args[0] === DYNAMIC_INIT) {
            const $dynamic$ = args[1]; // Useless but necessary to avoid a warning
            this.$dynamic$ = $dynamic$;

            Object.keys($dynamic$).forEach((key) => {
                this[key] = $dynamic$[key];
            });
            return;
        }
        // Check if this class is an extended class of $TemplateClassName$
        if (this instanceof $TemplateClassName$ && this.constructor !== $TemplateClassName$) {
            let Ext = Java.extend(
                _$TemplateJavaClassName$
            );

            let customInstance = new Ext(this);
            Object.keys(customInstance).forEach((key) => {
                this[key] = customInstance[key];
            });
        } else {
            let customInstance = new _$TemplateJavaClassName$(this);
            Object.keys(customInstance).forEach((key) => {
                this[key] = customInstance[key];
            });
        }
    }

    $StaticProperties$
    $StaticMethods$
    $Properties$
    $Methods$
}

//:::TEMPLATE_END

class TemplateClassForContent {
    $dynamic$

//:::TEMPLATE_START{"id":"method","properties":["MethodName"]}
    $MethodName$(...args) {
        return this.$dynamic$.$MethodName$(...args);
    }

//:::TEMPLATE_END
//:::TEMPLATE_START{"id":"property_getter","properties":["PropertyName"]}
    get $PropertyName$() {
        return this.$dynamic$.$PropertyName$;
    }

//:::TEMPLATE_END
//:::TEMPLATE_START{"id":"property_setter","properties":["PropertyName"]}
    set $PropertyName$(value) {
        this.$dynamic$.$PropertyName$ = value;
    }

//:::TEMPLATE_END
//:::TEMPLATE_START{"id":"static_method","properties":["MethodName","TemplateJavaClassName"]}
    static $MethodName$(...args) {
        return $DYNAMIC_INIT$_$ImportName$(_$TemplateJavaClassName$.$MethodName$(...args))
    }

//:::TEMPLATE_END
//:::TEMPLATE_START{"id":"static_method_primitive","properties":["MethodName","TemplateJavaClassName"]}
    static $MethodName$(...args) {
        return $JavaBoxedType$.valueOf(_$TemplateJavaClassName$.$MethodName$(...args)).$JavaPrimitiveType$Value();
    }

//:::TEMPLATE_END
//:::TEMPLATE_START{"id":"static_method_void","properties":["MethodName","TemplateJavaClassName"]}
    static $MethodName$(...args) {
        _$TemplateJavaClassName$.$MethodName$(...args);
    }

//:::TEMPLATE_END
//:::TEMPLATE_START{"id":"static_property_getter","properties":["PropertyName","TemplateJavaClassName"]}
    static get $PropertyName$() {
        return _$TemplateJavaClassName$.$PropertyName$;
    }

//:::TEMPLATE_END
//:::TEMPLATE_START{"id":"static_property_setter","properties":["PropertyName","TemplateJavaClassName"]}
    static set $PropertyName$(value) {
        _$TemplateJavaClassName$.$PropertyName$ = value;
    }

//:::TEMPLATE_END
//:::TEMPLATE_START{"id":"java_constant","properties":["ConstantName","TemplateJavaClassName"]}
    static $ConstantName$ = _$TemplateJavaClassName$.$ConstantName$;
//:::TEMPLATE_END
}
