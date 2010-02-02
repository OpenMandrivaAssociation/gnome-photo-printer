%define name	gnome-photo-printer
%define version	0.7.0
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	Simple Photo Printer for Gnome
Version: 	%{version}
Release: 	%{release}

Source:		gpp-%{version}.tar.bz2
Source1:	gpp-48.png
Source2:	gpp-32.png
Source3:	gpp-16.png
Patch0:		gpp-0.7.0-link.patch
URL:		http://www.fogman.de/?GnomePhotoPrinter
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	imagemagick
BuildRequires:	libgnomeui2-devel libglade2.0-devel
BuildRequires:	libgnomeprint-devel libgnomeprintui-devel
BuildRequires:	libgnome-vfs2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	intltool

%description
Gnome Photo Printer is intended for printing photos in an easy way.  Just
drag your Photos from Nautilus to the Gnome Photo Printer window and drop
it.  Make some selections like Photo or Paper size, hit Preview or Print,
and see your pictures printed.

%prep
%setup -q -n gpp-%version
%patch0 -p0 -b .link
mkdir m4

%build
autoreconf -fi
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gnome Photo Printer
Comment=Quick and simple photo printing
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-Multimedia-Graphics;Graphics;Photography;Viewer;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %{SOURCE1} > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %{SOURCE2} > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %{SOURCE3} > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/gnome-photo-printer.desktop
%{_datadir}/icons/hicolor/16x16/apps/gnome-photo-printer.png
%{_datadir}/icons/hicolor/22x22/apps/gnome-photo-printer.png
%{_datadir}/icons/hicolor/32x32/apps/gnome-photo-printer.png
%{_datadir}/icons/hicolor/48x48/apps/gnome-photo-printer.png
%{_datadir}/icons/hicolor/scalable/apps/gnome-photo-printer.svg



