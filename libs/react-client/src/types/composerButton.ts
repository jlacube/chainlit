export interface IComposerButton {
  id: string;
  label: string;
  style: 'primary' | 'secondary' | 'outline';
  data?: Record<string, any>;
}
