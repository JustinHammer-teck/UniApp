{
  description =
    "A Nix-flake-based python development environment - this only fit with my Intel-base MacBook";

  inputs = { nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable"; };

  outputs = { self, nixpkgs, ... }:
    let
      system = "x86_64-darwin";
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShells.x86_64-darwin.default = pkgs.mkShell {
        nativeBuildInputs = with pkgs;
          [ python312 virtualenv nodejs ] ++ (with pkgs.python312Packages; [
            pip
            python312Packages.python-dotenv
            python312Packages.tkinter
          ]);

        shellHook = ''
          echo "hello to python dev shell"
        '';

        PYTHON_PATH = "${pkgs.python312}/bin/python3:./src";
      };
    };
}
