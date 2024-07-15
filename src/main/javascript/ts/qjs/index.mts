export function extend(...types: Function[]): Function {
    function $(constructor: Function) {
        constructor["_superclasses"] = types
        return constructor
    }
    return $
}

export function base(baseClass: Function, self: any, ...args: any[]) {
    const superclasses: Function[] | undefined = self["_superclasses"] as Function[] | undefined;
    if (superclasses === undefined) {
        throw new Error("");
    }

    if (superclasses.includes(baseClass)) {
        baseClass(...args);
    } else {
        throw new TypeError(`Invalid type: ${baseClass.name}`);
    }
}
